from __future__ import annotations

import logging
import os
import pathlib
import pickle
import shutil
import unittest
from typing import TYPE_CHECKING, Dict, List, Optional, Union, cast
from unittest import mock

import pandas as pd
import pytest

import great_expectations as gx
import great_expectations.exceptions as gx_exceptions
from great_expectations.checkpoint import Checkpoint, LegacyCheckpoint, SimpleCheckpoint
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
from great_expectations.core import ExpectationSuiteValidationResult
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest
from great_expectations.core.config_peer import ConfigOutputModes
from great_expectations.core.expectation_validation_result import (
    ExpectationValidationResult,
)
from great_expectations.core.util import get_or_create_spark_application
from great_expectations.core.yaml_handler import YAMLHandler
from great_expectations.data_context import AbstractDataContext, FileDataContext
from great_expectations.data_context.types.base import (
    CheckpointConfig,
    checkpointConfigSchema,
)
from great_expectations.data_context.types.resource_identifiers import (
    ConfigurationIdentifier,
    ValidationResultIdentifier,
)
from great_expectations.render import RenderedAtomicContent
from great_expectations.util import (
    deep_filter_properties_iterable,
)
from great_expectations.validator.validator import Validator
from tests.checkpoint import cloud_config

if TYPE_CHECKING:
    from great_expectations.core.data_context_key import DataContextKey

yaml = YAMLHandler()

logger = logging.getLogger(__name__)


@pytest.fixture
def dummy_data_context() -> AbstractDataContext:
    class DummyDataContext:
        def __init__(self) -> None:
            self._usage_statistics_handler = None

    return cast(AbstractDataContext, DummyDataContext())


@pytest.fixture
def dummy_validator() -> Validator:
    class DummyValidator:
        @property
        def expectation_suite_name(self) -> str:
            return "my_expectation_suite"

    return cast(Validator, DummyValidator())


@pytest.fixture
def batch_request_as_dict() -> Dict[str, str]:
    return {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }


def test_checkpoint_raises_typeerror_on_incorrect_data_context():
    with pytest.raises(AttributeError):
        # noinspection PyTypeChecker
        Checkpoint(name="my_checkpoint", data_context="foo", config_version=1)


def test_checkpoint_with_no_config_version_has_no_action_list(empty_data_context):
    checkpoint: Checkpoint = Checkpoint(
        name="foo", data_context=empty_data_context, config_version=None
    )
    assert checkpoint.action_list == []


def test_checkpoint_with_config_version_has_action_list(empty_data_context):
    checkpoint: Checkpoint = Checkpoint(
        "foo", empty_data_context, config_version=1, action_list=[{"foo": "bar"}]
    )
    obs = checkpoint.action_list
    assert isinstance(obs, list)
    assert obs == [{"foo": "bar"}]


def test_add_custom_checkpoint_extensions(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    context.add_expectation_suite(expectation_suite_name="my_expectation_suite")

    checkpoint_config: dict = {
        "class_name": "ExtendedCheckpoint",
        "module_name": "extended_checkpoint",
        "name": "my_custom_extended_checkpoint",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }
    checkpoint = context.add_checkpoint(**checkpoint_config)
    assert issubclass(checkpoint.__class__, Checkpoint)
    assert checkpoint.__class__.__name__ == "ExtendedCheckpoint"

    checkpoint_config: dict = {
        "class_name": "ExtendedSimpleCheckpoint",
        "module_name": "extended_checkpoint",
        "name": "my_custom_extended_simple_checkpoint",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }
    checkpoint = context.add_checkpoint(**checkpoint_config)
    assert issubclass(checkpoint.__class__, SimpleCheckpoint)
    assert checkpoint.__class__.__name__ == "ExtendedSimpleCheckpoint"

    checkpoint_config: dict = {
        "class_name": "ExtendedLegacyCheckpoint",
        "module_name": "extended_checkpoint",
        "name": "my_custom_extended_legacy_checkpoint",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }
    with pytest.raises(gx_exceptions.InvalidCheckpointConfigError) as icpce:
        context.add_checkpoint(**checkpoint_config)

    assert (
        str(icpce.value)
        == 'Extending "LegacyCheckpoint" is not allowed, because "LegacyCheckpoint" is deprecated.'
    )

    checkpoint_config: dict = {
        "class_name": "ExtendedCheckpointIllegalBaseClass",
        "module_name": "extended_checkpoint",
        "name": "my_custom_extended_checkpoint_illegal_base_class",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }
    with pytest.raises(gx_exceptions.InvalidCheckpointConfigError) as icpce:
        context.add_checkpoint(**checkpoint_config)

    assert (
        str(icpce.value)
        == 'Custom class "ExtendedCheckpointIllegalBaseClass" must extend either "Checkpoint" or "SimpleCheckpoint" (exclusively).'
    )


@mock.patch(
    "great_expectations.core.usage_statistics.usage_statistics.UsageStatisticsHandler.emit"
)
def test_basic_checkpoint_config_validation(
    mock_emit,
    empty_data_context_stats_enabled,
    common_action_list,
    caplog,
    capsys,
):
    context: FileDataContext = empty_data_context_stats_enabled
    yaml_config_erroneous: str
    config_erroneous: dict
    checkpoint_config: Union[CheckpointConfig, dict]
    checkpoint: Checkpoint

    yaml_config_erroneous = """
    name: misconfigured_checkpoint
    unexpected_property: UNKNOWN_PROPERTY_VALUE
    """
    config_erroneous = yaml.load(yaml_config_erroneous)
    with pytest.raises(TypeError):
        # noinspection PyUnusedLocal
        checkpoint_config = CheckpointConfig(**config_erroneous)
    with pytest.raises(KeyError):
        # noinspection PyUnusedLocal
        checkpoint: Checkpoint = context.test_yaml_config(
            yaml_config=yaml_config_erroneous,
            name="my_erroneous_checkpoint",
        )

    assert mock_emit.call_count == 1

    # noinspection PyUnresolvedReferences
    expected_events: List[unittest.mock._Call]
    # noinspection PyUnresolvedReferences
    actual_events: List[unittest.mock._Call]

    expected_events = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
    ]
    actual_events = mock_emit.call_args_list
    assert actual_events == expected_events

    yaml_config_erroneous = """
    config_version: 1
    """
    config_erroneous = yaml.load(yaml_config_erroneous)
    with pytest.raises(gx_exceptions.InvalidConfigError):
        # noinspection PyUnusedLocal
        checkpoint_config = CheckpointConfig.from_commented_map(
            commented_map=config_erroneous
        )
    with pytest.raises(KeyError):
        # noinspection PyUnusedLocal
        checkpoint: Checkpoint = context.test_yaml_config(
            yaml_config=yaml_config_erroneous,
            name="my_erroneous_checkpoint",
        )

    assert mock_emit.call_count == 2

    expected_events = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
    ]
    actual_events = mock_emit.call_args_list
    assert actual_events == expected_events

    with pytest.raises(gx_exceptions.InvalidConfigError):
        # noinspection PyUnusedLocal
        checkpoint: Checkpoint = context.test_yaml_config(
            yaml_config=yaml_config_erroneous,
            name="my_erroneous_checkpoint",
            class_name="Checkpoint",
        )

    assert mock_emit.call_count == 3

    expected_events = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"parent_class": "Checkpoint"},
                "success": False,
            }
        ),
    ]
    actual_events = mock_emit.call_args_list
    assert actual_events == expected_events

    yaml_config_erroneous = """
    config_version: 1
    name: my_erroneous_checkpoint
    class_name: Checkpoint
    """
    # noinspection PyUnusedLocal
    checkpoint: Checkpoint = context.test_yaml_config(
        yaml_config=yaml_config_erroneous,
        name="my_erroneous_checkpoint",
        class_name="Checkpoint",
    )
    captured = capsys.readouterr()
    assert any(
        'Your current Checkpoint configuration has an empty or missing "validations" attribute'
        in message
        for message in [caplog.text, captured.out]
    )
    assert any(
        'Your current Checkpoint configuration has an empty or missing "action_list" attribute'
        in message
        for message in [caplog.text, captured.out]
    )

    assert mock_emit.call_count == 4

    # Substitute anonymized name since it changes for each run
    anonymized_name_0 = mock_emit.call_args_list[3][0][0]["event_payload"][
        "anonymized_name"
    ]

    expected_events = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"parent_class": "Checkpoint"},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {
                    "anonymized_name": anonymized_name_0,
                    "parent_class": "Checkpoint",
                },
                "success": True,
            }
        ),
    ]
    actual_events = mock_emit.call_args_list
    assert actual_events == expected_events

    assert len(context.list_checkpoints()) == 0
    context.add_checkpoint(**yaml.load(yaml_config_erroneous))
    assert len(context.list_checkpoints()) == 1

    yaml_config: str = """
    name: my_checkpoint
    config_version: 1
    class_name: Checkpoint
    validations: []
    action_list:
      - name: store_validation_result
        action:
          class_name: StoreValidationResultAction
      - name: store_evaluation_params
        action:
          class_name: StoreEvaluationParametersAction
      - name: update_data_docs
        action:
          class_name: UpdateDataDocsAction
    """

    expected_checkpoint_config: dict = {
        "name": "my_checkpoint",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "action_list": common_action_list,
    }

    config: dict = yaml.load(yaml_config)
    checkpoint_config = CheckpointConfig(**config)
    checkpoint: Checkpoint = Checkpoint(
        data_context=context,
        **deep_filter_properties_iterable(
            properties=checkpoint_config.to_json_dict(),
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        ),
    )
    filtered_expected_checkpoint_config: dict = deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        delete_fields={"class_name", "module_name"},
        clean_falsy=True,
    )
    assert (
        deep_filter_properties_iterable(
            properties=checkpoint.self_check()["config"],
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        )
        == filtered_expected_checkpoint_config
    )
    assert (
        deep_filter_properties_iterable(
            properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        )
        == filtered_expected_checkpoint_config
    )

    checkpoint: Checkpoint = context.test_yaml_config(
        yaml_config=yaml_config,
        name="my_checkpoint",
    )
    assert (
        deep_filter_properties_iterable(
            properties=checkpoint.self_check()["config"],
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        )
        == filtered_expected_checkpoint_config
    )
    assert (
        deep_filter_properties_iterable(
            properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        )
        == filtered_expected_checkpoint_config
    )

    assert mock_emit.call_count == 5

    # Substitute anonymized name since it changes for each run
    anonymized_name_1 = mock_emit.call_args_list[4][0][0]["event_payload"][
        "anonymized_name"
    ]

    expected_events = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"diagnostic_info": ["__class_name_not_provided__"]},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {"parent_class": "Checkpoint"},
                "success": False,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {
                    "anonymized_name": anonymized_name_0,
                    "parent_class": "Checkpoint",
                },
                "success": True,
            }
        ),
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {
                    "anonymized_name": anonymized_name_1,
                    "parent_class": "Checkpoint",
                },
                "success": True,
            }
        ),
    ]
    actual_events = mock_emit.call_args_list
    assert actual_events == expected_events

    assert len(context.list_checkpoints()) == 1
    context.add_checkpoint(**yaml.load(yaml_config))
    assert len(context.list_checkpoints()) == 2

    context.add_expectation_suite(expectation_suite_name="my_expectation_suite")
    with pytest.raises(
        gx_exceptions.DataContextError,
        match=r'Checkpoint "my_checkpoint" must be called with a validator or contain either a batch_request or validations.',
    ):
        context.run_checkpoint(
            checkpoint_name=checkpoint.name,
        )

    context.delete_checkpoint(name="my_erroneous_checkpoint")
    context.delete_checkpoint(name="my_checkpoint")
    assert len(context.list_checkpoints()) == 0


@pytest.mark.integration
@mock.patch(
    "great_expectations.core.usage_statistics.usage_statistics.UsageStatisticsHandler.emit"
)
def test_checkpoint_configuration_no_nesting_using_test_yaml_config(
    mock_emit,
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    monkeypatch,
):
    monkeypatch.setenv("VAR", "test")
    monkeypatch.setenv("MY_PARAM", "1")
    monkeypatch.setenv("OLD_PARAM", "2")

    checkpoint: Checkpoint

    data_context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    yaml_config: str = """
    name: my_fancy_checkpoint
    config_version: 1
    class_name: Checkpoint
    run_name_template: "%Y-%M-foo-bar-template-$VAR"
    validations:
      - batch_request:
          datasource_name: my_datasource
          data_connector_name: my_special_data_connector
          data_asset_name: users
          data_connector_query:
            index: -1
        expectation_suite_name: users.delivery
        action_list:
            - name: store_validation_result
              action:
                class_name: StoreValidationResultAction
            - name: store_evaluation_params
              action:
                class_name: StoreEvaluationParametersAction
            - name: update_data_docs
              action:
                class_name: UpdateDataDocsAction
    evaluation_parameters:
      param1: "$MY_PARAM"
      param2: 1 + "$OLD_PARAM"
    runtime_configuration:
      result_format:
        result_format: BASIC
        partial_unexpected_count: 20
    """

    expected_checkpoint_config: dict = {
        "name": "my_fancy_checkpoint",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -1,
                    },
                },
                "expectation_suite_name": "users.delivery",
                "action_list": common_action_list,
            },
        ],
        "evaluation_parameters": {"param1": "1", "param2": '1 + "2"'},
        "runtime_configuration": {
            "result_format": {
                "result_format": "BASIC",
                "partial_unexpected_count": 20,
            }
        },
        "template_name": None,
        "run_name_template": "%Y-%M-foo-bar-template-test",
        "expectation_suite_name": None,
        "batch_request": None,
        "action_list": [],
        "profilers": [],
    }

    checkpoint: Checkpoint = data_context.test_yaml_config(
        yaml_config=yaml_config,
        name="my_fancy_checkpoint",
    )
    assert deep_filter_properties_iterable(
        properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        clean_falsy=True,
    )

    # Test usage stats messages
    assert mock_emit.call_count == 1

    # Substitute current anonymized name since it changes for each run
    anonymized_checkpoint_name = mock_emit.call_args_list[0][0][0]["event_payload"][
        "anonymized_name"
    ]

    # noinspection PyUnresolvedReferences
    expected_events: List[unittest.mock._Call] = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {
                    "anonymized_name": anonymized_checkpoint_name,
                    "parent_class": "Checkpoint",
                },
                "success": True,
            }
        ),
    ]
    # noinspection PyUnresolvedReferences
    actual_events: List[unittest.mock._Call] = mock_emit.call_args_list
    assert actual_events == expected_events

    assert len(data_context.list_checkpoints()) == 0
    data_context.add_checkpoint(**yaml.load(yaml_config))
    assert len(data_context.list_checkpoints()) == 1

    data_context.add_expectation_suite(expectation_suite_name="users.delivery")
    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name=checkpoint.name,
    )
    assert len(result.list_validation_results()) == 1
    assert len(data_context.validations_store.list_keys()) == 1
    assert result.success

    data_context.delete_checkpoint(name="my_fancy_checkpoint")
    assert len(data_context.list_checkpoints()) == 0


@pytest.mark.integration
@pytest.mark.slow  # 1.74s
def test_checkpoint_configuration_nesting_provides_defaults_for_most_elements_test_yaml_config(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    monkeypatch,
):
    monkeypatch.setenv("VAR", "test")
    monkeypatch.setenv("MY_PARAM", "1")
    monkeypatch.setenv("OLD_PARAM", "2")

    checkpoint: Checkpoint

    data_context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    yaml_config: str = """
    name: my_fancy_checkpoint
    config_version: 1
    class_name: Checkpoint
    run_name_template: "%Y-%M-foo-bar-template-$VAR"
    validations:
      - batch_request:
          datasource_name: my_datasource
          data_connector_name: my_special_data_connector
          data_asset_name: users
          data_connector_query:
            index: -1
      - batch_request:
          datasource_name: my_datasource
          data_connector_name: my_other_data_connector
          data_asset_name: users
          data_connector_query:
            index: -2
    expectation_suite_name: users.delivery
    action_list:
        - name: store_validation_result
          action:
            class_name: StoreValidationResultAction
        - name: store_evaluation_params
          action:
            class_name: StoreEvaluationParametersAction
        - name: update_data_docs
          action:
            class_name: UpdateDataDocsAction
    evaluation_parameters:
      param1: "$MY_PARAM"
      param2: 1 + "$OLD_PARAM"
    runtime_configuration:
      result_format:
        result_format: BASIC
        partial_unexpected_count: 20
    """

    expected_checkpoint_config: dict = {
        "name": "my_fancy_checkpoint",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -1,
                    },
                }
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_other_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -2,
                    },
                }
            },
        ],
        "expectation_suite_name": "users.delivery",
        "action_list": common_action_list,
        "evaluation_parameters": {"param1": "1", "param2": '1 + "2"'},
        "runtime_configuration": {
            "result_format": {"result_format": "BASIC", "partial_unexpected_count": 20}
        },
        "template_name": None,
        "run_name_template": "%Y-%M-foo-bar-template-test",
        "batch_request": None,
        "profilers": [],
    }

    checkpoint: Checkpoint = data_context.test_yaml_config(
        yaml_config=yaml_config,
        name="my_fancy_checkpoint",
    )
    assert deep_filter_properties_iterable(
        properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        clean_falsy=True,
    )

    assert len(data_context.list_checkpoints()) == 0
    data_context.add_checkpoint(**yaml.load(yaml_config))
    assert len(data_context.list_checkpoints()) == 1

    data_context.add_expectation_suite(expectation_suite_name="users.delivery")
    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name=checkpoint.name,
    )
    assert len(result.list_validation_results()) == 2
    assert len(data_context.validations_store.list_keys()) == 2
    assert result.success

    data_context.delete_checkpoint(name="my_fancy_checkpoint")
    assert len(data_context.list_checkpoints()) == 0


@pytest.mark.integration
@mock.patch(
    "great_expectations.core.usage_statistics.usage_statistics.UsageStatisticsHandler.emit"
)
def test_checkpoint_configuration_using_RuntimeDataConnector_with_Airflow_test_yaml_config(
    mock_emit,
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    checkpoint: Checkpoint

    data_context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    yaml_config: str = """
    name: airflow_checkpoint
    config_version: 1
    class_name: Checkpoint
    validations:
    - batch_request:
        datasource_name: my_datasource
        data_connector_name: my_runtime_data_connector
        data_asset_name: IN_MEMORY_DATA_ASSET
    expectation_suite_name: users.delivery
    action_list:
        - name: store_validation_result
          action:
            class_name: StoreValidationResultAction
        - name: store_evaluation_params
          action:
            class_name: StoreEvaluationParametersAction
        - name: update_data_docs
          action:
            class_name: UpdateDataDocsAction
    """

    expected_checkpoint_config: dict = {
        "name": "airflow_checkpoint",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_runtime_data_connector",
                    "data_asset_name": "IN_MEMORY_DATA_ASSET",
                }
            }
        ],
        "expectation_suite_name": "users.delivery",
        "action_list": common_action_list,
        "template_name": None,
        "run_name_template": None,
        "batch_request": None,
        "evaluation_parameters": {},
        "runtime_configuration": {},
        "profilers": [],
    }

    checkpoint: Checkpoint = data_context.test_yaml_config(
        yaml_config=yaml_config,
        name="airflow_checkpoint",
    )
    assert deep_filter_properties_iterable(
        properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        clean_falsy=True,
    )

    assert len(data_context.list_checkpoints()) == 0
    data_context.add_checkpoint(**yaml.load(yaml_config))
    assert len(data_context.list_checkpoints()) == 1

    data_context.add_expectation_suite(expectation_suite_name="users.delivery")
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name=checkpoint.name,
        batch_request={
            "runtime_parameters": {
                "batch_data": test_df,
            },
            "batch_identifiers": {
                "airflow_run_id": 1234567890,
            },
        },
        run_name="airflow_run_1234567890",
    )
    assert len(result.list_validation_results()) == 1
    assert len(data_context.validations_store.list_keys()) == 1
    assert result.success

    assert mock_emit.call_count == 6

    # noinspection PyUnresolvedReferences
    expected_events: List[unittest.mock._Call] = [
        mock.call(
            {
                "event": "data_context.test_yaml_config",
                "event_payload": {
                    "anonymized_name": "f563d9aa1604e16099bb7dff7b203319",
                    "parent_class": "Checkpoint",
                },
                "success": True,
            },
        ),
        mock.call(
            {
                "event": "data_context.get_batch_list",
                "event_payload": {
                    "anonymized_batch_request_required_top_level_properties": {
                        "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                        "anonymized_data_connector_name": "d52d7bff3226a7f94dd3510c1040de78",
                        "anonymized_data_asset_name": "556e8c06239d09fc66f424eabb9ca491",
                    },
                    "batch_request_optional_top_level_keys": [
                        "batch_identifiers",
                        "runtime_parameters",
                    ],
                    "runtime_parameters_keys": ["batch_data"],
                },
                "success": True,
            },
        ),
        mock.call(
            {
                "event": "data_asset.validate",
                "event_payload": {
                    "anonymized_batch_kwarg_keys": [],
                    "anonymized_expectation_suite_name": "6a04fc37da0d43a4c21429f6788d2cff",
                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                },
                "success": True,
            }
        ),
        mock.call(
            {
                "event": "data_context.build_data_docs",
                "event_payload": {},
                "success": True,
            }
        ),
        mock.call(
            {
                "event": "checkpoint.run",
                "event_payload": {
                    "anonymized_name": "f563d9aa1604e16099bb7dff7b203319",
                    "config_version": 1.0,
                    "anonymized_expectation_suite_name": "6a04fc37da0d43a4c21429f6788d2cff",
                    "anonymized_action_list": [
                        {
                            "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                            "parent_class": "StoreValidationResultAction",
                        },
                        {
                            "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                            "parent_class": "StoreEvaluationParametersAction",
                        },
                        {
                            "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                            "parent_class": "UpdateDataDocsAction",
                        },
                    ],
                    "anonymized_validations": [
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "d52d7bff3226a7f94dd3510c1040de78",
                                    "anonymized_data_asset_name": "556e8c06239d09fc66f424eabb9ca491",
                                },
                                "batch_request_optional_top_level_keys": [
                                    "batch_identifiers",
                                    "runtime_parameters",
                                ],
                                "runtime_parameters_keys": ["batch_data"],
                            },
                            "anonymized_expectation_suite_name": "6a04fc37da0d43a4c21429f6788d2cff",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                    ],
                },
                "success": True,
            },
        ),
        mock.call(
            {
                "event": "data_context.run_checkpoint",
                "event_payload": {},
                "success": True,
            }
        ),
    ]
    # noinspection PyUnresolvedReferences
    actual_events: List[unittest.mock._Call] = mock_emit.call_args_list
    assert actual_events == expected_events

    data_context.delete_checkpoint(name="airflow_checkpoint")
    assert len(data_context.list_checkpoints()) == 0


@pytest.mark.integration
@pytest.mark.slow  # 1.75s
def test_checkpoint_configuration_warning_error_quarantine_test_yaml_config(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    monkeypatch,
):
    monkeypatch.setenv("GE_ENVIRONMENT", "my_ge_environment")

    checkpoint: Checkpoint

    data_context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    yaml_config: str = """
    name: airflow_users_node_3
    config_version: 1
    class_name: Checkpoint
    batch_request:
        datasource_name: my_datasource
        data_connector_name: my_special_data_connector
        data_asset_name: users
        data_connector_query:
            index: -1
    validations:
      - expectation_suite_name: users.warning  # runs the top-level action list against the top-level batch_request
      - expectation_suite_name: users.error  # runs the locally-specified action_list union the top level action-list against the top-level batch_request
        action_list:
        - name: quarantine_failed_data
          action:
              class_name: CreateQuarantineData
        - name: advance_passed_data
          action:
              class_name: CreatePassedData
    action_list:
        - name: store_validation_result
          action:
            class_name: StoreValidationResultAction
        - name: store_evaluation_params
          action:
            class_name: StoreEvaluationParametersAction
        - name: update_data_docs
          action:
            class_name: UpdateDataDocsAction
    evaluation_parameters:
        environment: $GE_ENVIRONMENT
        tolerance: 0.01
    runtime_configuration:
        result_format:
          result_format: BASIC
          partial_unexpected_count: 20
    """

    mock_create_quarantine_data = mock.MagicMock()
    mock_create_quarantine_data.run.return_value = True
    # noinspection PyUnresolvedReferences
    gx.validation_operators.CreateQuarantineData = mock_create_quarantine_data

    mock_create_passed_data = mock.MagicMock()
    mock_create_passed_data.run.return_value = True
    # noinspection PyUnresolvedReferences
    gx.validation_operators.CreatePassedData = mock_create_passed_data

    expected_checkpoint_config: dict = {
        "name": "airflow_users_node_3",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "batch_request": {
            "datasource_name": "my_datasource",
            "data_connector_name": "my_special_data_connector",
            "data_asset_name": "users",
            "data_connector_query": {
                "index": -1,
            },
        },
        "validations": [
            {"expectation_suite_name": "users.warning"},
            {
                "expectation_suite_name": "users.error",
                "action_list": [
                    {
                        "name": "quarantine_failed_data",
                        "action": {"class_name": "CreateQuarantineData"},
                    },
                    {
                        "name": "advance_passed_data",
                        "action": {"class_name": "CreatePassedData"},
                    },
                ],
            },
        ],
        "action_list": common_action_list,
        "evaluation_parameters": {
            "environment": "my_ge_environment",
            "tolerance": 0.01,
        },
        "runtime_configuration": {
            "result_format": {"result_format": "BASIC", "partial_unexpected_count": 20}
        },
        "template_name": None,
        "run_name_template": None,
        "expectation_suite_name": None,
        "profilers": [],
    }

    checkpoint: Checkpoint = data_context.test_yaml_config(
        yaml_config=yaml_config,
        name="airflow_users_node_3",
    )
    assert deep_filter_properties_iterable(
        properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        clean_falsy=True,
    )

    assert len(data_context.list_checkpoints()) == 0
    data_context.add_checkpoint(**yaml.load(yaml_config))
    assert len(data_context.list_checkpoints()) == 1

    data_context.add_expectation_suite(expectation_suite_name="users.warning")
    data_context.add_expectation_suite(expectation_suite_name="users.error")
    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name=checkpoint.name,
    )
    assert len(result.list_validation_results()) == 2
    assert len(data_context.validations_store.list_keys()) == 2
    assert result.success

    data_context.delete_checkpoint(name="airflow_users_node_3")
    assert len(data_context.list_checkpoints()) == 0


@pytest.mark.integration
@pytest.mark.slow  # 3.10s
def test_checkpoint_configuration_template_parsing_and_usage_test_yaml_config(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    monkeypatch,
):
    monkeypatch.setenv("VAR", "test")
    monkeypatch.setenv("MY_PARAM", "1")
    monkeypatch.setenv("OLD_PARAM", "2")

    checkpoint: Checkpoint
    yaml_config: str
    expected_checkpoint_config: dict
    result: CheckpointResult

    data_context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    yaml_config = """
    name: my_base_checkpoint
    config_version: 1
    class_name: Checkpoint
    run_name_template: "%Y-%M-foo-bar-template-$VAR"
    action_list:
    - name: store_validation_result
      action:
        class_name: StoreValidationResultAction
    - name: store_evaluation_params
      action:
        class_name: StoreEvaluationParametersAction
    - name: update_data_docs
      action:
        class_name: UpdateDataDocsAction
    evaluation_parameters:
      param1: "$MY_PARAM"
      param2: 1 + "$OLD_PARAM"
    runtime_configuration:
        result_format:
          result_format: BASIC
          partial_unexpected_count: 20
    """

    expected_checkpoint_config = {
        "name": "my_base_checkpoint",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "template_name": None,
        "run_name_template": "%Y-%M-foo-bar-template-test",
        "expectation_suite_name": None,
        "batch_request": None,
        "action_list": common_action_list,
        "evaluation_parameters": {"param1": "1", "param2": '1 + "2"'},
        "runtime_configuration": {
            "result_format": {"result_format": "BASIC", "partial_unexpected_count": 20}
        },
        "validations": [],
        "profilers": [],
    }

    checkpoint: Checkpoint = data_context.test_yaml_config(
        yaml_config=yaml_config,
        name="my_base_checkpoint",
    )
    assert deep_filter_properties_iterable(
        properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        clean_falsy=True,
    )

    assert len(data_context.list_checkpoints()) == 0
    data_context.add_checkpoint(**yaml.load(yaml_config))
    assert len(data_context.list_checkpoints()) == 1

    with pytest.raises(
        gx_exceptions.DataContextError,
        match=r'Checkpoint "my_base_checkpoint" must be called with a validator or contain either a batch_request or validations.',
    ):
        # noinspection PyUnusedLocal
        result: CheckpointResult = data_context.run_checkpoint(
            checkpoint_name=checkpoint.name,
        )

    data_context.add_expectation_suite(expectation_suite_name="users.delivery")

    result = data_context.run_checkpoint(
        checkpoint_name="my_base_checkpoint",
        validations=[
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -1,
                    },
                },
                "expectation_suite_name": "users.delivery",
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_other_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -2,
                    },
                },
                "expectation_suite_name": "users.delivery",
            },
        ],
    )
    assert len(result.list_validation_results()) == 2
    assert len(data_context.validations_store.list_keys()) == 2
    assert result.success

    yaml_config = """
    name: my_fancy_checkpoint
    config_version: 1
    class_name: Checkpoint
    template_name: my_base_checkpoint
    validations:
    - batch_request:
        datasource_name: my_datasource
        data_connector_name: my_special_data_connector
        data_asset_name: users
        data_connector_query:
          index: -1
    - batch_request:
        datasource_name: my_datasource
        data_connector_name: my_other_data_connector
        data_asset_name: users
        data_connector_query:
          index: -2
    expectation_suite_name: users.delivery
    """

    expected_checkpoint_config = {
        "name": "my_fancy_checkpoint",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "template_name": "my_base_checkpoint",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -1,
                    },
                }
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_other_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {
                        "index": -2,
                    },
                }
            },
        ],
        "expectation_suite_name": "users.delivery",
        "run_name_template": None,
        "batch_request": None,
        "action_list": [],
        "evaluation_parameters": {},
        "runtime_configuration": {},
        "profilers": [],
    }

    checkpoint: Checkpoint = data_context.test_yaml_config(
        yaml_config=yaml_config,
        name="my_fancy_checkpoint",
    )
    assert deep_filter_properties_iterable(
        properties=checkpoint.get_config(mode=ConfigOutputModes.DICT),
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_checkpoint_config,
        clean_falsy=True,
    )

    assert len(data_context.list_checkpoints()) == 1
    data_context.add_checkpoint(**yaml.load(yaml_config))
    assert len(data_context.list_checkpoints()) == 2

    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name=checkpoint.name,
    )
    assert len(result.list_validation_results()) == 2
    assert len(data_context.validations_store.list_keys()) == 4
    assert result.success

    data_context.delete_checkpoint(name="my_base_checkpoint")
    data_context.delete_checkpoint(name="my_fancy_checkpoint")
    assert len(data_context.list_checkpoints()) == 0


@pytest.mark.integration
@pytest.mark.slow  # 1.05s
def test_legacy_checkpoint_instantiates_and_produces_a_validation_result_when_run(
    filesystem_csv_data_context_with_validation_operators,
    common_action_list,
):
    rad_datasource = list(
        filter(
            lambda element: element["name"] == "rad_datasource",
            filesystem_csv_data_context_with_validation_operators.list_datasources(),
        )
    )[0]
    base_directory = rad_datasource["batch_kwargs_generators"]["subdir_reader"][
        "base_directory"
    ]
    batch_kwargs: dict = {
        "path": base_directory + "/f1.csv",
        "datasource": "rad_datasource",
        "reader_method": "read_csv",
    }

    checkpoint_config_dict: dict = {
        "name": "my_checkpoint",
        "validation_operator_name": "action_list_operator",
        "batches": [
            {"batch_kwargs": batch_kwargs, "expectation_suite_names": ["my_suite"]}
        ],
    }

    checkpoint: LegacyCheckpoint = LegacyCheckpoint(
        data_context=filesystem_csv_data_context_with_validation_operators,
        **checkpoint_config_dict,
    )

    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        checkpoint.run()

    assert (
        len(
            filesystem_csv_data_context_with_validation_operators.validations_store.list_keys()
        )
        == 0
    )

    filesystem_csv_data_context_with_validation_operators.add_expectation_suite(
        "my_suite"
    )
    checkpoint.run()

    assert (
        len(
            filesystem_csv_data_context_with_validation_operators.validations_store.list_keys()
        )
        == 1
    )


@pytest.mark.integration
@pytest.mark.slow  # 1.25s
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    # add checkpoint config
    checkpoint_config = CheckpointConfig(
        name="my_checkpoint",
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        validations=[
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_basic_data_connector",
                    "data_asset_name": "Titanic_1911",
                }
            }
        ],
    )
    checkpoint_config_key = ConfigurationIdentifier(
        configuration_key=checkpoint_config.name
    )
    context.checkpoint_store.set(key=checkpoint_config_key, value=checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(checkpoint_config.name)

    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        checkpoint.run()

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_with_checkpoint_name_in_meta_when_run(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    store_validation_result_action,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    checkpoint_name: str = "test_checkpoint_name"
    # add checkpoint config
    checkpoint_config = CheckpointConfig(
        name=checkpoint_name,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=[
            store_validation_result_action,
        ],
        validations=[
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_basic_data_connector",
                    "data_asset_name": "Titanic_1911",
                }
            }
        ],
    )
    checkpoint_config_key = ConfigurationIdentifier(
        configuration_key=checkpoint_config.name
    )
    context.checkpoint_store.set(key=checkpoint_config_key, value=checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(checkpoint_config.name)

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    result: CheckpointResult = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]

    validation_result_identifier: DataContextKey = (
        context.validations_store.list_keys()[0]
    )
    validation_result: ExpectationSuiteValidationResult = context.validations_store.get(
        validation_result_identifier
    )

    assert "checkpoint_name" in validation_result.meta
    assert validation_result.meta["checkpoint_name"] == checkpoint_name


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_batch_request_and_validator_are_specified_in_constructor(
    dummy_data_context,
    common_action_list,
    dummy_validator,
    batch_request_as_dict,
):
    context = dummy_data_context
    validator = dummy_validator

    batch_request: BatchRequest = BatchRequest(**batch_request_as_dict)
    with pytest.raises(
        gx_exceptions.CheckpointError,
        match=r'Checkpoint "my_checkpoint" cannot be called with a validator and contain a batch_request and/or a batch_request in validations.',
    ):
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            expectation_suite_name="my_expectation_suite",
            batch_request=batch_request,
            validator=validator,
            action_list=common_action_list,
        )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_batch_request_in_validations_and_validator_are_specified_in_constructor(
    dummy_data_context,
    common_action_list,
    dummy_validator,
    batch_request_as_dict,
):
    context = dummy_data_context
    validator = dummy_validator

    batch_request: BatchRequest = BatchRequest(**batch_request_as_dict)
    with pytest.raises(
        gx_exceptions.CheckpointError,
        match=r'Checkpoint "my_checkpoint" cannot be called with a validator and contain a batch_request and/or a batch_request in validations.',
    ):
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            expectation_suite_name="my_expectation_suite",
            validator=validator,
            action_list=common_action_list,
            validations=[{"batch_request": batch_request}],
        )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_expectation_suite_name_and_validator_are_specified_in_constructor(
    dummy_data_context,
    common_action_list,
    dummy_validator,
    batch_request_as_dict,
):
    context = dummy_data_context
    validator = dummy_validator

    with pytest.raises(
        gx_exceptions.CheckpointError,
        match=r'Checkpoint "my_checkpoint" cannot be called with a validator and contain an expectation_suite_name and/or an expectation_suite_name in validations.',
    ):
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            expectation_suite_name="my_expectation_suite",
            validator=validator,
            action_list=common_action_list,
        )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_expectation_suite_name_in_validations_and_validator_are_specified_in_constructor(
    dummy_data_context,
    common_action_list,
    dummy_validator,
):
    context = dummy_data_context
    validator = dummy_validator

    with pytest.raises(
        gx_exceptions.CheckpointError,
        match=r'Checkpoint "my_checkpoint" cannot be called with a validator and contain an expectation_suite_name and/or an expectation_suite_name in validations.',
    ):
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            validator=validator,
            action_list=common_action_list,
            validations=[{"expectation_suite_name": "my_expectation_suite"}],
        )


@pytest.mark.integration
@pytest.mark.slow  # 1.15s
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_with_validator_specified_in_constructor(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    batch_request_as_dict,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    batch_request: BatchRequest = BatchRequest(**batch_request_as_dict)
    context.add_expectation_suite("my_expectation_suite")
    validator: Validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite_name="my_expectation_suite",
    )
    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        validator=validator,
        action_list=common_action_list,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_validator_specified_in_constructor_and_validator_is_specified_in_run(
    dummy_data_context,
    common_action_list,
    dummy_validator,
):
    context = dummy_data_context
    validator = dummy_validator

    with pytest.raises(gx_exceptions.CheckpointError) as e:
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            validator=validator,
            action_list=common_action_list,
        ).run(
            validator=validator,
        )

    assert (
        str(e.value)
        == 'Checkpoint "my_checkpoint" has already been created with a validator and overriding it through run() is not allowed.'
    )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_validator_specified_in_constructor_and_validator_is_specified_in_run(  # noqa: F811 # TODO: review test for duplication
    dummy_data_context,
    common_action_list,
    dummy_validator,
):
    context = dummy_data_context
    validator = dummy_validator

    with pytest.raises(gx_exceptions.CheckpointError) as e:
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            validator=validator,
            action_list=common_action_list,
        ).run(
            validator=validator,
        )

    assert (
        str(e.value)
        == 'Checkpoint "my_checkpoint" has already been created with a validator and overriding it through run() is not allowed.'
    )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_batch_request_is_specified_in_validations_and_batch_request_and_validator_are_specified_in_run(
    dummy_data_context,
    common_action_list,
    dummy_validator,
    batch_request_as_dict,
):
    context = dummy_data_context
    validator = dummy_validator

    batch_request: BatchRequest = BatchRequest(**batch_request_as_dict)
    with pytest.raises(gx_exceptions.CheckpointError) as e:
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            expectation_suite_name="my_expectation_suite",
            action_list=common_action_list,
            validations=[{"batch_request": batch_request}],
        ).run(
            batch_request=batch_request_as_dict,
            validator=validator,
        )

    assert (
        str(e.value)
        == 'Checkpoint "my_checkpoint" has already been created with a validator and overriding it by supplying a batch_request and/or validations with a batch_request to run() is not allowed.'
    )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_validator_specified_in_constructor_and_expectation_suite_name_is_specified_in_run(
    dummy_data_context,
    common_action_list,
    dummy_validator,
):
    context = dummy_data_context
    validator = dummy_validator

    with pytest.raises(gx_exceptions.CheckpointError) as e:
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            validator=validator,
            action_list=common_action_list,
        ).run(
            expectation_suite_name="my_expectation_suite",
        )

    assert (
        str(e.value)
        == 'Checkpoint "my_checkpoint" has already been created with a validator and overriding its expectation_suite_name by supplying an expectation_suite_name and/or validations with an expectation_suite_name to run() is not allowed.'
    )


@pytest.mark.unit
def test_newstyle_checkpoint_raises_error_if_expectation_suite_name_is_specified_in_validations_and_validator_is_specified_in_run(
    dummy_data_context,
    common_action_list,
    dummy_validator,
    batch_request_as_dict,
):
    context = dummy_data_context
    validator = dummy_validator

    batch_request: BatchRequest = BatchRequest(**batch_request_as_dict)
    with pytest.raises(gx_exceptions.CheckpointError) as e:
        _ = Checkpoint(
            name="my_checkpoint",
            data_context=context,
            config_version=1,
            run_name_template="%Y-%M-foo-bar-template",
            expectation_suite_name="my_expectation_suite",
            action_list=common_action_list,
            validations=[{"batch_request": batch_request}],
        ).run(
            batch_request=batch_request_as_dict,
            validator=validator,
        )

    assert (
        str(e.value)
        == 'Checkpoint "my_checkpoint" has already been created with a validator and overriding it by supplying a batch_request and/or validations with a batch_request to run() is not allowed.'
    )


@pytest.mark.integration
@pytest.mark.slow  # 1.15s
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_with_validator_specified_in_run(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    batch_request_as_dict,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    batch_request: BatchRequest = BatchRequest(**batch_request_as_dict)
    context.add_expectation_suite("my_expectation_suite")
    validator: Validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite_name="my_expectation_suite",
    )
    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(
        validator=validator,
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.15s
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_batch_request_object(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
    batch_request_as_dict,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    # add checkpoint config
    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }
    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        validations=[{"batch_request": batch_request}],
    )
    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        checkpoint.run()

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_object_pandasdf(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "test_df",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )
    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )
    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_object_sparkdf(
    data_context_with_datasource_spark_engine,
    common_action_list,
    spark_session,
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "test_df",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )
    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )
    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        # noinspection PyUnusedLocal
        result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@mock.patch(
    "great_expectations.core.usage_statistics.usage_statistics.UsageStatisticsHandler.emit"
)
@pytest.mark.slow  # 1.31s
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_batch_request_object_multi_validation_pandasdf(
    mock_emit,
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "test_df",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )
    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        # noinspection PyUnusedLocal
        result = checkpoint.run(
            validations=[
                {"batch_request": runtime_batch_request},
                {"batch_request": batch_request},
            ]
        )

    assert mock_emit.call_count == 1
    # noinspection PyUnresolvedReferences
    expected_events: List[unittest.mock._Call] = [
        mock.call(
            {
                "event_payload": {
                    "anonymized_name": "d7e22c0913c0cb83d528d2a7ad097f2b",
                    "config_version": 1,
                    "anonymized_run_name_template": "131f67e5ea07d59f2bc5376234f7f9f2",
                    "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                    "anonymized_action_list": [
                        {
                            "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                            "parent_class": "StoreValidationResultAction",
                        },
                        {
                            "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                            "parent_class": "StoreEvaluationParametersAction",
                        },
                        {
                            "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                            "parent_class": "UpdateDataDocsAction",
                        },
                    ],
                    "anonymized_validations": [
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "d52d7bff3226a7f94dd3510c1040de78",
                                    "anonymized_data_asset_name": "7e60092b1b9b96327196fdba39029b9e",
                                },
                                "batch_request_optional_top_level_keys": [
                                    "batch_identifiers",
                                    "runtime_parameters",
                                ],
                                "runtime_parameters_keys": ["batch_data"],
                            },
                            "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "af09acd176f54642635a8a2975305437",
                                    "anonymized_data_asset_name": "38b9086d45a8746d014a0d63ad58e331",
                                }
                            },
                            "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                    ],
                },
                "event": "checkpoint.run",
                "success": False,
            }
        )
    ]
    # noinspection PyUnresolvedReferences
    actual_events: List[unittest.mock._Call] = mock_emit.call_args_list
    assert actual_events == expected_events

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    # noinspection PyUnusedLocal
    result = checkpoint.run(
        validations=[
            {"batch_request": runtime_batch_request},
            {"batch_request": batch_request},
        ]
    )

    assert len(context.validations_store.list_keys()) == 2
    assert result["success"]

    assert mock_emit.call_count == 8

    # noinspection PyUnresolvedReferences
    expected_events: List[unittest.mock._Call] = [
        mock.call(
            {
                "event_payload": {
                    "anonymized_name": "d7e22c0913c0cb83d528d2a7ad097f2b",
                    "config_version": 1,
                    "anonymized_run_name_template": "131f67e5ea07d59f2bc5376234f7f9f2",
                    "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                    "anonymized_action_list": [
                        {
                            "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                            "parent_class": "StoreValidationResultAction",
                        },
                        {
                            "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                            "parent_class": "StoreEvaluationParametersAction",
                        },
                        {
                            "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                            "parent_class": "UpdateDataDocsAction",
                        },
                    ],
                    "anonymized_validations": [
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "d52d7bff3226a7f94dd3510c1040de78",
                                    "anonymized_data_asset_name": "7e60092b1b9b96327196fdba39029b9e",
                                },
                                "batch_request_optional_top_level_keys": [
                                    "batch_identifiers",
                                    "runtime_parameters",
                                ],
                                "runtime_parameters_keys": ["batch_data"],
                            },
                            "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "af09acd176f54642635a8a2975305437",
                                    "anonymized_data_asset_name": "38b9086d45a8746d014a0d63ad58e331",
                                },
                            },
                            "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                    ],
                },
                "event": "checkpoint.run",
                "success": False,
            }
        ),
        mock.call(
            {
                "event_payload": {
                    "anonymized_batch_request_required_top_level_properties": {
                        "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                        "anonymized_data_connector_name": "d52d7bff3226a7f94dd3510c1040de78",
                        "anonymized_data_asset_name": "7e60092b1b9b96327196fdba39029b9e",
                    },
                    "batch_request_optional_top_level_keys": [
                        "batch_identifiers",
                        "runtime_parameters",
                    ],
                    "runtime_parameters_keys": ["batch_data"],
                },
                "event": "data_context.get_batch_list",
                "success": True,
            }
        ),
        mock.call(
            {
                "event": "data_asset.validate",
                "event_payload": {
                    "anonymized_batch_kwarg_keys": [],
                    "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                },
                "success": True,
            }
        ),
        mock.call(
            {
                "event_payload": {},
                "event": "data_context.build_data_docs",
                "success": True,
            }
        ),
        mock.call(
            {
                "event_payload": {
                    "anonymized_batch_request_required_top_level_properties": {
                        "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                        "anonymized_data_connector_name": "af09acd176f54642635a8a2975305437",
                        "anonymized_data_asset_name": "38b9086d45a8746d014a0d63ad58e331",
                    }
                },
                "event": "data_context.get_batch_list",
                "success": True,
            }
        ),
        mock.call(
            {
                "event": "data_asset.validate",
                "event_payload": {
                    "anonymized_batch_kwarg_keys": [],
                    "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                },
                "success": True,
            }
        ),
        mock.call(
            {
                "event_payload": {},
                "event": "data_context.build_data_docs",
                "success": True,
            }
        ),
        mock.call(
            {
                "event_payload": {
                    "anonymized_name": "d7e22c0913c0cb83d528d2a7ad097f2b",
                    "config_version": 1,
                    "anonymized_run_name_template": "131f67e5ea07d59f2bc5376234f7f9f2",
                    "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                    "anonymized_action_list": [
                        {
                            "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                            "parent_class": "StoreValidationResultAction",
                        },
                        {
                            "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                            "parent_class": "StoreEvaluationParametersAction",
                        },
                        {
                            "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                            "parent_class": "UpdateDataDocsAction",
                        },
                    ],
                    "anonymized_validations": [
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "d52d7bff3226a7f94dd3510c1040de78",
                                    "anonymized_data_asset_name": "7e60092b1b9b96327196fdba39029b9e",
                                },
                                "batch_request_optional_top_level_keys": [
                                    "batch_identifiers",
                                    "runtime_parameters",
                                ],
                                "runtime_parameters_keys": ["batch_data"],
                            },
                            "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                        {
                            "anonymized_batch_request": {
                                "anonymized_batch_request_required_top_level_properties": {
                                    "anonymized_datasource_name": "a732a247720783a5931fa7c4606403c2",
                                    "anonymized_data_connector_name": "af09acd176f54642635a8a2975305437",
                                    "anonymized_data_asset_name": "38b9086d45a8746d014a0d63ad58e331",
                                },
                            },
                            "anonymized_expectation_suite_name": "295722d0683963209e24034a79235ba6",
                            "anonymized_action_list": [
                                {
                                    "anonymized_name": "8e3e134cd0402c3970a02f40d2edfc26",
                                    "parent_class": "StoreValidationResultAction",
                                },
                                {
                                    "anonymized_name": "40e24f0c6b04b6d4657147990d6f39bd",
                                    "parent_class": "StoreEvaluationParametersAction",
                                },
                                {
                                    "anonymized_name": "2b99b6b280b8a6ad1176f37580a16411",
                                    "parent_class": "UpdateDataDocsAction",
                                },
                            ],
                        },
                    ],
                },
                "event": "checkpoint.run",
                "success": True,
            }
        ),
    ]
    # noinspection PyUnresolvedReferences
    actual_events: List[unittest.mock._Call] = mock_emit.call_args_list
    assert actual_events == expected_events

    # Since there are two validations, confirming there should be two "data_asset.validate" events
    num_data_asset_validate_events = 0
    for event in actual_events:
        if event[0][0]["event"] == "data_asset.validate":
            num_data_asset_validate_events += 1
    assert num_data_asset_validate_events == 2


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_batch_request_object_multi_validation_sparkdf(
    data_context_with_datasource_spark_engine,
    common_action_list,
    spark_session,
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df_1 = spark_session.createDataFrame(pandas_df)
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [5, 6], "col2": [7, 8]})
    test_df_2 = spark_session.createDataFrame(pandas_df)

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request_1: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "test_df_1",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df_1},
        }
    )

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request_2: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "test_df_2",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df_2},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )
    with pytest.raises(
        gx_exceptions.DataContextError, match=r"expectation_suite .* not found"
    ):
        # noinspection PyUnusedLocal
        result = checkpoint.run(
            validations=[
                {"batch_request": runtime_batch_request_1},
                {"batch_request": runtime_batch_request_2},
            ]
        )

    assert len(context.validations_store.list_keys()) == 0

    context.add_expectation_suite("my_expectation_suite")
    # noinspection PyUnusedLocal
    result = checkpoint.run(
        validations=[
            {"batch_request": runtime_batch_request_1},
            {"batch_request": runtime_batch_request_2},
        ]
    )

    assert len(context.validations_store.list_keys()) == 2
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.08s
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_single_runtime_batch_request_query_in_validations(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        validations=[{"batch_request": runtime_batch_request}],
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_multiple_runtime_batch_request_query_in_validations(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query 1
    batch_request_1 = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    # RuntimeBatchRequest with a query 2
    batch_request_2 = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 5"
            },
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        validations=[
            {"batch_request": batch_request_1},
            {"batch_request": batch_request_2},
        ],
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_raise_error_when_run_when_missing_batch_request_and_validations(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    with pytest.raises(
        gx_exceptions.CheckpointError,
        match='Checkpoint "my_checkpoint" must be called with a validator or contain either a batch_request or validations.',
    ):
        checkpoint.run()


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_query_in_top_level_batch_request(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        batch_request=runtime_batch_request,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_top_level_batch_request_pandasdf(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=runtime_batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_top_level_batch_request_sparkdf(
    data_context_with_datasource_spark_engine,
    common_action_list,
    spark_session,
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=runtime_batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.slow  # 1.09s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_top_level_batch_request_pandas(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        batch_request=runtime_batch_request,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_top_level_batch_request_spark(
    titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        batch_request=runtime_batch_request,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_config_substitution_simple(
    monkeypatch,
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
    common_action_list,
):
    monkeypatch.setenv("GE_ENVIRONMENT", "my_ge_environment")
    monkeypatch.setenv("VAR", "test")
    monkeypatch.setenv("MY_PARAM", "1")
    monkeypatch.setenv("OLD_PARAM", "2")

    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates

    simplified_checkpoint_config = CheckpointConfig(
        name="my_simplified_checkpoint",
        config_version=1,
        template_name="my_simple_template_checkpoint",
        expectation_suite_name="users.delivery",
        validations=[
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {"partition_index": -1},
                }
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_other_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {"partition_index": -2},
                }
            },
        ],
    )
    simplified_checkpoint: Checkpoint = Checkpoint(
        data_context=context,
        **deep_filter_properties_iterable(
            properties=simplified_checkpoint_config.to_json_dict(),
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        ),
    )

    # template only
    expected_substituted_checkpoint_config_template_only: CheckpointConfig = (
        CheckpointConfig(
            name="my_simplified_checkpoint",
            config_version=1.0,
            run_name_template="%Y-%M-foo-bar-template-test",
            expectation_suite_name="users.delivery",
            action_list=common_action_list,
            evaluation_parameters={
                "environment": "my_ge_environment",
                "tolerance": 1.0e-2,
                "aux_param_0": "1",
                "aux_param_1": "1 + 1",
            },
            runtime_configuration={
                "result_format": {
                    "result_format": "BASIC",
                    "partial_unexpected_count": 20,
                }
            },
            validations=[
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_special_data_connector",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -1},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -2},
                    }
                },
            ],
        )
    )

    substituted_config_template_only: dict = (
        simplified_checkpoint.get_substituted_config()
    )
    filtered_expected_substituted_checkpoint_config_template_only: dict = deep_filter_properties_iterable(
        properties=expected_substituted_checkpoint_config_template_only.to_json_dict(),
        clean_falsy=True,
    )
    assert (
        deep_filter_properties_iterable(
            properties=substituted_config_template_only,
            clean_falsy=True,
        )
        == filtered_expected_substituted_checkpoint_config_template_only
    )
    assert (
        deep_filter_properties_iterable(
            properties=substituted_config_template_only,
            clean_falsy=True,
        )
        == filtered_expected_substituted_checkpoint_config_template_only
    )

    # template and runtime kwargs
    expected_substituted_checkpoint_config_template_and_runtime_kwargs = (
        CheckpointConfig(
            name="my_simplified_checkpoint",
            config_version=1,
            run_name_template="runtime_run_template",
            expectation_suite_name="runtime_suite_name",
            action_list=[
                {
                    "name": "store_validation_result",
                    "action": {
                        "class_name": "StoreValidationResultAction",
                    },
                },
                {
                    "name": "store_evaluation_params",
                    "action": {
                        "class_name": "MyCustomStoreEvaluationParametersAction",
                    },
                },
                {
                    "name": "update_data_docs_deluxe",
                    "action": {
                        "class_name": "UpdateDataDocsAction",
                    },
                },
            ],
            evaluation_parameters={
                "environment": "runtime-my_ge_environment",
                "tolerance": 1.0e-2,
                "aux_param_0": "runtime-1",
                "aux_param_1": "1 + 1",
                "new_runtime_eval_param": "bloopy!",
            },
            runtime_configuration={
                "result_format": {
                    "result_format": "BASIC",
                    "partial_unexpected_count": 999,
                    "new_runtime_config_key": "bleepy!",
                }
            },
            validations=[
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_special_data_connector",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -1},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -2},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector_2",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -3},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector_3",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -4},
                    }
                },
            ],
        )
    )

    substituted_config_template_and_runtime_kwargs = (
        simplified_checkpoint.get_substituted_config(
            runtime_kwargs={
                "expectation_suite_name": "runtime_suite_name",
                "validations": [
                    {
                        "batch_request": {
                            "datasource_name": "my_datasource",
                            "data_connector_name": "my_other_data_connector_2",
                            "data_asset_name": "users",
                            "data_connector_query": {"partition_index": -3},
                        }
                    },
                    {
                        "batch_request": {
                            "datasource_name": "my_datasource",
                            "data_connector_name": "my_other_data_connector_3",
                            "data_asset_name": "users",
                            "data_connector_query": {"partition_index": -4},
                        }
                    },
                ],
                "run_name_template": "runtime_run_template",
                "action_list": [
                    {
                        "name": "store_validation_result",
                        "action": {
                            "class_name": "StoreValidationResultAction",
                        },
                    },
                    {
                        "name": "store_evaluation_params",
                        "action": {
                            "class_name": "MyCustomStoreEvaluationParametersAction",
                        },
                    },
                    {
                        "name": "update_data_docs",
                        "action": None,
                    },
                    {
                        "name": "update_data_docs_deluxe",
                        "action": {
                            "class_name": "UpdateDataDocsAction",
                        },
                    },
                ],
                "evaluation_parameters": {
                    "environment": "runtime-$GE_ENVIRONMENT",
                    "tolerance": 1.0e-2,
                    "aux_param_0": "runtime-$MY_PARAM",
                    "aux_param_1": "1 + $MY_PARAM",
                    "new_runtime_eval_param": "bloopy!",
                },
                "runtime_configuration": {
                    "result_format": {
                        "result_format": "BASIC",
                        "partial_unexpected_count": 999,
                        "new_runtime_config_key": "bleepy!",
                    }
                },
            }
        )
    )
    assert deep_filter_properties_iterable(
        properties=substituted_config_template_and_runtime_kwargs,
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_substituted_checkpoint_config_template_and_runtime_kwargs.to_json_dict(),
        clean_falsy=True,
    )


@pytest.mark.integration
def test_newstyle_checkpoint_config_substitution_nested(
    monkeypatch,
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
    common_action_list,
):
    monkeypatch.setenv("GE_ENVIRONMENT", "my_ge_environment")
    monkeypatch.setenv("VAR", "test")
    monkeypatch.setenv("MY_PARAM", "1")
    monkeypatch.setenv("OLD_PARAM", "2")

    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates

    nested_checkpoint_config = CheckpointConfig(
        name="my_nested_checkpoint",
        config_version=1,
        template_name="my_nested_checkpoint_template_2",
        expectation_suite_name="users.delivery",
        validations=[
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {"partition_index": -1},
                }
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_other_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {"partition_index": -2},
                }
            },
        ],
    )
    nested_checkpoint: Checkpoint = Checkpoint(
        data_context=context,
        **deep_filter_properties_iterable(
            properties=nested_checkpoint_config.to_json_dict(),
            delete_fields={"class_name", "module_name"},
            clean_falsy=True,
        ),
    )

    # template only
    expected_nested_checkpoint_config_template_only = CheckpointConfig(
        name="my_nested_checkpoint",
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template-test-template-2",
        expectation_suite_name="users.delivery",
        action_list=[
            {
                "name": "store_validation_result",
                "action": {
                    "class_name": "StoreValidationResultAction",
                },
            },
            {
                "name": "store_evaluation_params",
                "action": {
                    "class_name": "MyCustomStoreEvaluationParametersActionTemplate2",
                },
            },
            {
                "name": "update_data_docs",
                "action": {
                    "class_name": "UpdateDataDocsAction",
                },
            },
            {
                "name": "new_action_from_template_2",
                "action": {"class_name": "Template2SpecialAction"},
            },
        ],
        evaluation_parameters={
            "environment": "my_ge_environment",
            "tolerance": 1.0e-2,
            "aux_param_0": "1",
            "aux_param_1": "1 + 1",
            "template_1_key": 456,
        },
        runtime_configuration={
            "result_format": "BASIC",
            "partial_unexpected_count": 20,
            "template_1_key": 123,
        },
        validations=[
            {
                "batch_request": {
                    "datasource_name": "my_datasource_template_1",
                    "data_connector_name": "my_special_data_connector_template_1",
                    "data_asset_name": "users_from_template_1",
                    "data_connector_query": {"partition_index": -999},
                }
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {"partition_index": -1},
                }
            },
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_other_data_connector",
                    "data_asset_name": "users",
                    "data_connector_query": {"partition_index": -2},
                }
            },
        ],
    )

    substituted_config_template_only = nested_checkpoint.get_substituted_config()
    filtered_expected_nested_checkpoint_config_template_only: dict = (
        deep_filter_properties_iterable(
            properties=expected_nested_checkpoint_config_template_only.to_json_dict(),
            clean_falsy=True,
        )
    )
    assert (
        deep_filter_properties_iterable(
            properties=substituted_config_template_only,
            clean_falsy=True,
        )
        == filtered_expected_nested_checkpoint_config_template_only
    )
    assert (
        deep_filter_properties_iterable(
            properties=substituted_config_template_only,
            clean_falsy=True,
        )
        == filtered_expected_nested_checkpoint_config_template_only
    )

    # runtime kwargs with new checkpoint template name passed at runtime
    expected_nested_checkpoint_config_template_and_runtime_template_name = (
        CheckpointConfig(
            name="my_nested_checkpoint",
            config_version=1,
            template_name="my_nested_checkpoint_template_3",
            run_name_template="runtime_run_template",
            expectation_suite_name="runtime_suite_name",
            action_list=[
                {
                    "name": "store_validation_result",
                    "action": {
                        "class_name": "StoreValidationResultAction",
                    },
                },
                {
                    "name": "store_evaluation_params",
                    "action": {
                        "class_name": "MyCustomRuntimeStoreEvaluationParametersAction",
                    },
                },
                {
                    "name": "new_action_from_template_2",
                    "action": {"class_name": "Template2SpecialAction"},
                },
                {
                    "name": "new_action_from_template_3",
                    "action": {"class_name": "Template3SpecialAction"},
                },
                {
                    "name": "update_data_docs_deluxe_runtime",
                    "action": {
                        "class_name": "UpdateDataDocsAction",
                    },
                },
            ],
            evaluation_parameters={
                "environment": "runtime-my_ge_environment",
                "tolerance": 1.0e-2,
                "aux_param_0": "runtime-1",
                "aux_param_1": "1 + 1",
                "template_1_key": 456,
                "template_3_key": 123,
                "new_runtime_eval_param": "bloopy!",
            },
            runtime_configuration={
                "result_format": "BASIC",
                "partial_unexpected_count": 999,
                "template_1_key": 123,
                "template_3_key": "bloopy!",
                "new_runtime_config_key": "bleepy!",
            },
            validations=[
                {
                    "batch_request": {
                        "datasource_name": "my_datasource_template_1",
                        "data_connector_name": "my_special_data_connector_template_1",
                        "data_asset_name": "users_from_template_1",
                        "data_connector_query": {"partition_index": -999},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_special_data_connector",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -1},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -2},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector_2_runtime",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -3},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector_3_runtime",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -4},
                    }
                },
            ],
        )
    )

    substituted_config_template_and_runtime_kwargs = nested_checkpoint.get_substituted_config(
        runtime_kwargs={
            "expectation_suite_name": "runtime_suite_name",
            "template_name": "my_nested_checkpoint_template_3",
            "validations": [
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector_2_runtime",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -3},
                    }
                },
                {
                    "batch_request": {
                        "datasource_name": "my_datasource",
                        "data_connector_name": "my_other_data_connector_3_runtime",
                        "data_asset_name": "users",
                        "data_connector_query": {"partition_index": -4},
                    }
                },
            ],
            "run_name_template": "runtime_run_template",
            "action_list": [
                {
                    "name": "store_validation_result",
                    "action": {
                        "class_name": "StoreValidationResultAction",
                    },
                },
                {
                    "name": "store_evaluation_params",
                    "action": {
                        "class_name": "MyCustomRuntimeStoreEvaluationParametersAction",
                    },
                },
                {
                    "name": "update_data_docs",
                    "action": None,
                },
                {
                    "name": "update_data_docs_deluxe_runtime",
                    "action": {
                        "class_name": "UpdateDataDocsAction",
                    },
                },
            ],
            "evaluation_parameters": {
                "environment": "runtime-$GE_ENVIRONMENT",
                "tolerance": 1.0e-2,
                "aux_param_0": "runtime-$MY_PARAM",
                "aux_param_1": "1 + $MY_PARAM",
                "new_runtime_eval_param": "bloopy!",
            },
            "runtime_configuration": {
                "result_format": "BASIC",
                "partial_unexpected_count": 999,
                "new_runtime_config_key": "bleepy!",
            },
        }
    )
    assert deep_filter_properties_iterable(
        properties=substituted_config_template_and_runtime_kwargs,
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_nested_checkpoint_config_template_and_runtime_template_name.to_json_dict(),
        clean_falsy=True,
    )


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_query_in_checkpoint_run(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=runtime_batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_query_in_checkpoint_run(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.slow  # 1.11s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_checkpoint_run_pandas(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=runtime_batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_checkpoint_run_spark(
    titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=runtime_batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_checkpoint_run_pandas(  # noqa: F811 # TODO: review test for duplication
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_path_in_checkpoint_run_spark(
    titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_query_in_context_run_checkpoint(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=runtime_batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_context_run_checkpoint_pandasdf(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=runtime_batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_context_run_checkpoint_sparkdf(
    data_context_with_datasource_spark_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = get_or_create_spark_application().createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=runtime_batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_query_in_context_run_checkpoint(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {
                "query": "SELECT * from table_partitioned_by_date_column__A LIMIT 10"
            },
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint",
        validations=[{"batch_request": runtime_batch_request}],
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_batch_data_in_context_run_checkpoint_pandasdf(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint",
        validations=[{"batch_request": runtime_batch_request}],
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_batch_data_in_context_run_checkpoint_sparkdf(
    data_context_with_datasource_spark_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = get_or_create_spark_application().createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint",
        validations=[{"batch_request": runtime_batch_request}],
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.slow  # 1.18s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_context_run_checkpoint_pandas(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=runtime_batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_context_run_checkpoint_spark(
    titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=runtime_batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_context_run_checkpoint_pandas(  # noqa: F811 # TODO: review test for duplication
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint",
        validations=[{"batch_request": runtime_batch_request}],
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_path_in_context_run_checkpoint_spark(
    titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_spark_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled

    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint",
        validations=[{"batch_request": runtime_batch_request}],
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_printable_validation_result_with_batch_data(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: Checkpoint = Checkpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=runtime_batch_request)

    assert type(repr(result)) == str


@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_runtime_parameters_error_contradictory_batch_request_in_checkpoint_yml_and_checkpoint_run(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    data_path: str = os.path.join(  # noqa: PTH118
        context.datasources["my_datasource"]
        .data_connectors["my_basic_data_connector"]
        .base_directory,
        "Titanic_19120414_1313.csv",
    )

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a path
    # Using typed object instead of dictionary, expected by "add_checkpoint()", on purpose to insure that checks work.
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"path": data_path},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": batch_request,
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "Titanic_19120414_1313.csv",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    with pytest.raises(
        gx_exceptions.exceptions.InvalidBatchRequestError,
        match=r"The runtime_parameters dict must have one \(and only one\) of the following keys: 'batch_data', 'query', 'path'.",
    ):
        checkpoint.run(batch_request=runtime_batch_request)


@pytest.mark.slow  # 1.75s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_correct_validation_result_batch_request_in_checkpoint_yml_and_checkpoint_run(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "test_df",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": batch_request,
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    result = checkpoint.run()
    assert not result["success"]
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 0
    )

    result = checkpoint.run(batch_request=runtime_batch_request)
    assert result["success"]
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 1
    )


@pytest.mark.slow  # 2.35s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_correct_validation_result_validations_in_checkpoint_yml_and_checkpoint_run(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "test_df",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [{"batch_request": batch_request}],
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    result = checkpoint.run()
    assert result["success"] is False
    assert len(result.run_results.values()) == 1
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 0
    )

    result = checkpoint.run(validations=[{"batch_request": runtime_batch_request}])
    assert result["success"] is False
    assert len(result.run_results.values()) == 2
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 0
    )
    assert (
        list(result.run_results.values())[1]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[1]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 1
    )


@pytest.mark.slow  # 1.91s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_correct_validation_result_batch_request_in_checkpoint_yml_and_context_run_checkpoint(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "test_df",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": batch_request,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(checkpoint_name="my_checkpoint")
    assert result["success"] is False
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 0
    )

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=runtime_batch_request
    )
    assert result["success"]
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 1
    )


@pytest.mark.slow  # 2.46s
@pytest.mark.integration
def test_newstyle_checkpoint_instantiates_and_produces_a_correct_validation_result_validations_in_checkpoint_yml_and_context_run_checkpoint(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "my_runtime_data_connector",
            "data_asset_name": "test_df",
            "batch_identifiers": {
                "pipeline_stage_name": "core_processing",
                "airflow_run_id": 1234567890,
            },
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [{"batch_request": batch_request}],
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(checkpoint_name="my_checkpoint")
    assert result["success"] is False
    assert len(result.run_results.values()) == 1
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 0
    )

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint",
        validations=[{"batch_request": runtime_batch_request}],
    )
    assert result["success"] is False
    assert len(result.run_results.values()) == 2
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[0]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 0
    )
    assert (
        list(result.run_results.values())[1]["validation_result"]["statistics"][
            "evaluated_expectations"
        ]
        == 1
    )
    assert (
        list(result.run_results.values())[1]["validation_result"]["statistics"][
            "successful_expectations"
        ]
        == 1
    )


@pytest.mark.integration
def test_newstyle_checkpoint_does_not_pass_dataframes_via_batch_request_into_checkpoint_store(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": batch_request,
    }

    with pytest.raises(
        gx_exceptions.InvalidConfigError,
        match='batch_data found in batch_request cannot be saved to CheckpointStore "checkpoint_store"',
    ):
        context.add_checkpoint(**checkpoint_config)


@pytest.mark.integration
def test_newstyle_checkpoint_does_not_pass_dataframes_via_validations_into_checkpoint_store(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a DataFrame
    runtime_batch_request: RuntimeBatchRequest = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [{"batch_request": runtime_batch_request}],
    }

    with pytest.raises(
        gx_exceptions.InvalidConfigError,
        match='batch_data found in validations cannot be saved to CheckpointStore "checkpoint_store"',
    ):
        context.add_checkpoint(**checkpoint_config)


@pytest.mark.slow  # 1.19s
@pytest.mark.integration
def test_newstyle_checkpoint_result_can_be_pickled(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": batch_request,
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    result: CheckpointResult = checkpoint.run()
    assert isinstance(pickle.dumps(result), bytes)


@pytest.mark.integration
@pytest.mark.slow  # 1.19s
@pytest.mark.integration
def test_newstyle_checkpoint_result_validations_include_rendered_content(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    include_rendered_content: bool = True

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [
            {
                "batch_request": batch_request,
                "include_rendered_content": include_rendered_content,
            }
        ],
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    result: CheckpointResult = checkpoint.run()
    validation_result_identifier: ValidationResultIdentifier = (
        result.list_validation_result_identifiers()[0]
    )
    expectation_validation_result: ExpectationValidationResult | dict = (
        result.run_results[validation_result_identifier]["validation_result"]
    )
    for result in expectation_validation_result.results:
        for rendered_content in result.rendered_content:
            assert isinstance(rendered_content, RenderedAtomicContent)


@pytest.mark.integration
@pytest.mark.slow  # 1.22s
def test_newstyle_checkpoint_result_validations_include_rendered_content_data_context_variable(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
    common_action_list,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    context.include_rendered_content.globally = True

    # add checkpoint config
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [
            {
                "batch_request": batch_request,
            }
        ],
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    result: CheckpointResult = checkpoint.run()
    validation_result_identifier: ValidationResultIdentifier = (
        result.list_validation_result_identifiers()[0]
    )
    expectation_validation_result: ExpectationValidationResult | dict = (
        result.run_results[validation_result_identifier]["validation_result"]
    )
    for result in expectation_validation_result.results:
        for rendered_content in result.rendered_content:
            assert isinstance(rendered_content, RenderedAtomicContent)


@pytest.mark.integration
@pytest.mark.parametrize(
    "checkpoint_config,expected_validation_id",
    [
        pytest.param(
            CheckpointConfig(
                name="my_checkpoint",
                config_version=1,
                run_name_template="%Y-%M-foo-bar-template",
                expectation_suite_name="my_expectation_suite",
                action_list=[
                    {
                        "name": "store_validation_result",
                        "action": {
                            "class_name": "StoreValidationResultAction",
                        },
                    },
                ],
                validations=[
                    {
                        "batch_request": {
                            "datasource_name": "my_datasource",
                            "data_connector_name": "my_basic_data_connector",
                            "data_asset_name": "Titanic_1911",
                        },
                    },
                ],
            ),
            None,
            id="no ids",
        ),
        pytest.param(
            CheckpointConfig(
                name="my_checkpoint",
                config_version=1,
                default_validation_id="7e2bb5c9-cdbe-4c7a-9b2b-97192c55c95b",
                run_name_template="%Y-%M-foo-bar-template",
                expectation_suite_name="my_expectation_suite",
                batch_request={
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_basic_data_connector",
                    "data_asset_name": "Titanic_1911",
                },
                action_list=[
                    {
                        "name": "store_validation_result",
                        "action": {
                            "class_name": "StoreValidationResultAction",
                        },
                    },
                ],
                validations=[],
            ),
            "7e2bb5c9-cdbe-4c7a-9b2b-97192c55c95b",
            id="default validation id",
        ),
        pytest.param(
            CheckpointConfig(
                name="my_checkpoint",
                config_version=1,
                run_name_template="%Y-%M-foo-bar-template",
                expectation_suite_name="my_expectation_suite",
                action_list=[
                    {
                        "name": "store_validation_result",
                        "action": {
                            "class_name": "StoreValidationResultAction",
                        },
                    },
                ],
                validations=[
                    {
                        "id": "f22601d9-00b7-4d54-beb6-605d87a74e40",
                        "batch_request": {
                            "datasource_name": "my_datasource",
                            "data_connector_name": "my_basic_data_connector",
                            "data_asset_name": "Titanic_1911",
                        },
                    },
                ],
            ),
            "f22601d9-00b7-4d54-beb6-605d87a74e40",
            id="nested validation id",
        ),
        pytest.param(
            CheckpointConfig(
                name="my_checkpoint",
                config_version=1,
                default_validation_id="7e2bb5c9-cdbe-4c7a-9b2b-97192c55c95b",
                run_name_template="%Y-%M-foo-bar-template",
                expectation_suite_name="my_expectation_suite",
                action_list=[
                    {
                        "name": "store_validation_result",
                        "action": {
                            "class_name": "StoreValidationResultAction",
                        },
                    },
                ],
                validations=[
                    {
                        "id": "f22601d9-00b7-4d54-beb6-605d87a74e40",
                        "batch_request": {
                            "datasource_name": "my_datasource",
                            "data_connector_name": "my_basic_data_connector",
                            "data_asset_name": "Titanic_1911",
                        },
                    },
                ],
            ),
            "f22601d9-00b7-4d54-beb6-605d87a74e40",
            id="both default and nested validation id",
        ),
    ],
)
def test_checkpoint_run_adds_validation_ids_to_expectation_suite_validation_result_meta(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation: FileDataContext,
    common_action_list,
    checkpoint_config: CheckpointConfig,
    expected_validation_id: str,
) -> None:
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation

    checkpoint_config_dict: dict = checkpointConfigSchema.dump(checkpoint_config)
    context.add_checkpoint(**checkpoint_config_dict)
    checkpoint: Checkpoint = context.get_checkpoint(name="my_checkpoint")

    result: CheckpointResult = checkpoint.run()

    # Always have a single validation result based on the test's parametrization
    validation_result: ExpectationValidationResult | dict = tuple(
        result.run_results.values()
    )[0]["validation_result"]

    actual_validation_id: Optional[str] = validation_result.meta["validation_id"]
    assert expected_validation_id == actual_validation_id


@pytest.fixture()
def _fake_cloud_context_setup(tmp_path, monkeypatch):
    data_dir = tmp_path
    # When setting up a checkpoint, we validate that there is data in the data directory
    # so we create a file.
    data_file = "yellow_tripdata_sample_2019-01.csv"
    data_file_path = (
        pathlib.Path(__file__)
        / ".."
        / ".."
        / "test_sets"
        / "taxi_yellow_tripdata_samples"
        / data_file
    ).resolve()
    shutil.copy(str(data_file_path), data_dir)

    monkeypatch.setenv("GX_CLOUD_BASE_URL", "https://my_cloud_backend.com")
    monkeypatch.setenv(
        "GX_CLOUD_ORGANIZATION_ID", "11111111-1111-1111-1111-123456789012"
    )
    monkeypatch.setenv("GX_CLOUD_ACCESS_TOKEN", "token")

    monkeypatch.setattr(
        gx.data_context.CloudDataContext,
        "retrieve_data_context_config_from_cloud",
        cloud_config.make_retrieve_data_context_config_from_cloud(data_dir),
    )
    monkeypatch.setattr(
        gx.data_context.store.gx_cloud_store_backend.GXCloudStoreBackend,
        "_set",
        cloud_config.store_set,
    )
    monkeypatch.setattr(
        gx.data_context.store.gx_cloud_store_backend.GXCloudStoreBackend,
        "list_keys",
        cloud_config.list_keys,
    )
    yield data_dir, data_file


@pytest.fixture()
def fake_cloud_context_basic(_fake_cloud_context_setup, monkeypatch):
    data_dir, data_file = _fake_cloud_context_setup
    monkeypatch.setattr(
        gx.data_context.store.gx_cloud_store_backend.GXCloudStoreBackend,
        "_get",
        cloud_config.make_store_get(data_file, with_slack=False),
    )
    context = gx.data_context.CloudDataContext()
    yield context


@pytest.fixture()
def fake_cloud_context_with_slack(_fake_cloud_context_setup, monkeypatch):
    data_dir, data_file = _fake_cloud_context_setup
    monkeypatch.setattr(
        gx.data_context.store.gx_cloud_store_backend.GXCloudStoreBackend,
        "_get",
        cloud_config.make_store_get(data_file, with_slack=True),
    )
    slack_counter = cloud_config.CallCounter()
    monkeypatch.setattr(
        gx.checkpoint.actions,
        "send_slack_notification",
        cloud_config.make_send_slack_notifications(slack_counter),
    )
    context = gx.data_context.CloudDataContext()
    yield context, slack_counter


@pytest.mark.integration
@pytest.mark.cloud
def test_use_validation_url_from_cloud(fake_cloud_context_basic):
    context = fake_cloud_context_basic
    checkpoint_name = "my_checkpoint"
    checkpoint = context.get_checkpoint(checkpoint_name)
    checkpoint_result = context.run_checkpoint(ge_cloud_id=checkpoint.ge_cloud_id)
    org_id = os.environ["GX_CLOUD_ORGANIZATION_ID"]
    assert (
        checkpoint_result.validation_result_url
        == f"https://my_cloud_backend.com/{org_id}/?validationResultId=2e13ecc3-eaaa-444b-b30d-2f616f80ae35"
    )


@pytest.mark.integration
@pytest.mark.cloud
def test_use_validation_url_from_cloud_with_slack(fake_cloud_context_with_slack):
    context, slack_counter = fake_cloud_context_with_slack
    checkpoint_name = "my_checkpoint"
    checkpoint = context.get_checkpoint(checkpoint_name)
    context.run_checkpoint(ge_cloud_id=checkpoint.ge_cloud_id)
    assert slack_counter.count == 1


### SparkDF Tests
@pytest.mark.integration
def test_running_spark_checkpoint(
    context_with_single_csv_spark_and_suite,
    common_action_list,
    spark_df_taxi_data_schema,
):
    context = context_with_single_csv_spark_and_suite
    single_batch_batch_request: BatchRequest = BatchRequest(
        datasource_name="my_datasource",
        data_connector_name="configured_data_connector_multi_batch_asset",
        data_asset_name="yellow_tripdata_2020",
        batch_spec_passthrough={
            "reader_options": {
                "header": True,
            }
        },
    )
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [
            {
                "batch_request": single_batch_batch_request,
            }
        ],
    }
    context.add_checkpoint(**checkpoint_config)
    results = context.run_checkpoint(checkpoint_name="my_checkpoint")
    assert results.success is True


@pytest.mark.integration
def test_run_spark_checkpoint_with_schema(
    context_with_single_csv_spark_and_suite,
    common_action_list,
    spark_df_taxi_data_schema,
):
    context = context_with_single_csv_spark_and_suite
    single_batch_batch_request: BatchRequest = BatchRequest(
        datasource_name="my_datasource",
        data_connector_name="configured_data_connector_multi_batch_asset",
        data_asset_name="yellow_tripdata_2020",
        batch_spec_passthrough={
            "reader_options": {
                "header": True,
                "schema": spark_df_taxi_data_schema,
            }
        },
    )
    checkpoint_config: dict = {
        "class_name": "Checkpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [
            {
                "batch_request": single_batch_batch_request,
            }
        ],
    }
    context.add_checkpoint(**checkpoint_config)
    results = context.run_checkpoint(checkpoint_name="my_checkpoint")

    assert results.success is True
