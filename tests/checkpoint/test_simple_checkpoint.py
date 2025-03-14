import copy
import os
from typing import Dict, List, Union, cast

import pandas as pd
import pytest

import great_expectations.exceptions as gx_exceptions
from great_expectations.checkpoint import SimpleCheckpointConfigurator
from great_expectations.checkpoint.checkpoint import (
    Checkpoint,
    CheckpointResult,
    LegacyCheckpoint,
    SimpleCheckpoint,
)
from great_expectations.core import ExpectationValidationResult
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest
from great_expectations.core.config_peer import ConfigOutputModes
from great_expectations.data_context import FileDataContext
from great_expectations.data_context.types.base import CheckpointConfig
from great_expectations.data_context.types.resource_identifiers import (
    ValidationResultIdentifier,
)
from great_expectations.render import RenderedAtomicContent
from great_expectations.util import deep_filter_properties_iterable


@pytest.fixture
def context_with_data_source_and_empty_suite(
    titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled,
):
    context: FileDataContext = titanic_pandas_data_context_with_v013_datasource_with_checkpoints_v1_with_empty_store_stats_enabled
    datasources = context.list_datasources()
    assert datasources[0]["class_name"] == "Datasource"
    assert "my_special_data_connector" in datasources[0]["data_connectors"].keys()
    context.add_expectation_suite("one")
    assert context.list_expectation_suite_names() == ["one"]
    return context


@pytest.fixture
def simple_checkpoint_defaults(
    context_with_data_source_and_empty_suite,
) -> SimpleCheckpoint:
    return SimpleCheckpoint(
        name="foo", data_context=context_with_data_source_and_empty_suite
    )


@pytest.fixture
def batch_request_as_dict() -> Dict[str, str]:
    return {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_special_data_connector",
        "data_asset_name": "users",
    }


@pytest.fixture
def one_validation(
    batch_request_as_dict: Dict[str, str]
) -> Dict[str, Union[str, Dict[str, str]]]:
    return {
        "batch_request": batch_request_as_dict,
        "expectation_suite_name": "one",
    }


@pytest.fixture
def two_validations(
    one_validation: Dict[str, Union[str, Dict[str, str]]]
) -> List[Dict[str, Union[str, Dict[str, str]]]]:
    second_validation: Dict[str, Union[str, Dict[str, str]]] = copy.deepcopy(
        one_validation
    )
    second_validation["expectation_suite_name"] = "two"
    return [
        one_validation,
        second_validation,
    ]


@pytest.mark.integration
def test_simple_checkpoint_default_properties_with_no_optional_arguments(
    empty_data_context,
    common_action_list,
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
):
    """This demonstrates the simplest possible usage."""
    checkpoint_config = SimpleCheckpointConfigurator(
        "my_minimal_simple_checkpoint", empty_data_context
    ).build()
    assert isinstance(checkpoint_config, CheckpointConfig)

    assert checkpoint_config.name == "my_minimal_simple_checkpoint"
    assert checkpoint_config.action_list == common_action_list
    assert checkpoint_config.config_version == 1.0
    assert checkpoint_config.class_name == "Checkpoint"
    assert checkpoint_config.evaluation_parameters == {}
    assert checkpoint_config.runtime_configuration == {}
    assert checkpoint_config.validations == []

    checkpoint_from_store = titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates.get_checkpoint(
        "my_minimal_simple_checkpoint"
    )
    checkpoint_config = checkpoint_from_store.get_config(mode=ConfigOutputModes.DICT)
    assert checkpoint_config["name"] == "my_minimal_simple_checkpoint"
    assert checkpoint_config["action_list"] == common_action_list
    assert checkpoint_config["config_version"] == 1.0
    assert checkpoint_config["evaluation_parameters"] == {}
    assert checkpoint_config["runtime_configuration"] == {}
    assert checkpoint_config["validations"] == []


def test_simple_checkpoint_raises_error_on_invalid_slack_webhook(
    empty_data_context,
):
    with pytest.raises(ValueError):
        SimpleCheckpointConfigurator(
            "foo", empty_data_context, slack_webhook="bad"
        ).build()


@pytest.mark.integration
def test_simple_checkpoint_has_slack_action_with_defaults_when_slack_webhook_is_present(
    empty_data_context,
    common_action_list,
    slack_notification_action,
    webhook,
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
):
    checkpoint_config = SimpleCheckpointConfigurator(
        "foo", empty_data_context, slack_webhook=webhook
    ).build()
    expected = common_action_list + [slack_notification_action]
    assert checkpoint_config.action_list == expected

    checkpoint_from_store = titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates.get_checkpoint(
        "my_simple_checkpoint_with_slack"
    )
    checkpoint_config = checkpoint_from_store.get_config(mode=ConfigOutputModes.DICT)
    assert checkpoint_config["name"] == "my_simple_checkpoint_with_slack"
    assert checkpoint_config["action_list"] == expected


def test_simple_checkpoint_raises_error_on_invalid_notify_on(
    empty_data_context,
):
    for bad in [1, "bar", None, []]:
        with pytest.raises(ValueError):
            SimpleCheckpointConfigurator(
                "foo", empty_data_context, notify_on=bad
            ).build()


def test_simple_checkpoint_raises_error_on_missing_slack_webhook_when_notify_on_is_list(
    empty_data_context, slack_notification_action, webhook
):
    with pytest.raises(ValueError):
        SimpleCheckpointConfigurator(
            "foo", empty_data_context, notify_with=["prod", "dev"]
        ).build()


def test_simple_checkpoint_raises_error_on_missing_slack_webhook_when_notify_on_is_not_default(
    empty_data_context, slack_notification_action, webhook
):
    for condition in ["failure", "success"]:
        with pytest.raises(ValueError):
            SimpleCheckpointConfigurator(
                "foo", empty_data_context, notify_on=condition
            ).build()


def test_simple_checkpoint_raises_error_on_invalid_notify_with(
    empty_data_context,
):
    for bad in [1, "bar", ["local_site", 3]]:
        with pytest.raises(ValueError):
            SimpleCheckpointConfigurator(
                "foo", empty_data_context, notify_with=bad
            ).build()


@pytest.mark.integration
def test_simple_checkpoint_notify_with_all_has_data_docs_action_with_none_specified(
    empty_data_context,
    slack_notification_action,
    webhook,
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
):
    """
    The underlying SlackNotificationAction and SlackRenderer default to
    including links to all sites if the key notify_with is not present. We are
    intentionally hiding this from users of SimpleCheckpoint by having a default
    of "all" that sets the configuration appropriately.
    """
    checkpoint_config: Union[CheckpointConfig, dict] = SimpleCheckpointConfigurator(
        "foo", empty_data_context, slack_webhook=webhook, notify_with="all"
    ).build()

    # set the config to include all sites
    slack_notification_action["action"]["notify_with"] = None
    assert slack_notification_action in checkpoint_config.action_list

    checkpoint_from_store: Checkpoint = titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates.get_checkpoint(
        "my_simple_checkpoint_with_slack_and_notify_with_all"
    )
    checkpoint_config = checkpoint_from_store.get_config(mode=ConfigOutputModes.DICT)
    assert slack_notification_action in checkpoint_config["action_list"]


def test_simple_checkpoint_has_slack_action_with_notify_adjustments_slack_webhook_is_present(
    empty_data_context,
    store_validation_result_action,
    store_eval_parameter_action,
    update_data_docs_action,
    slack_notification_action,
    webhook,
):
    checkpoint_config = SimpleCheckpointConfigurator(
        "foo",
        empty_data_context,
        slack_webhook=webhook,
        notify_on="failure",
        notify_with=["local_site", "s3_prod"],
    ).build()

    slack_notification_action["action"]["notify_on"] = "failure"
    slack_notification_action["action"]["notify_with"] = ["local_site", "s3_prod"]  # type: ignore[return-value]
    expected = [
        store_validation_result_action,
        store_eval_parameter_action,
        update_data_docs_action,
        slack_notification_action,
    ]
    assert checkpoint_config.action_list == expected


def test_simple_checkpoint_has_no_slack_action_when_no_slack_webhook_is_present(
    empty_data_context,
    common_action_list,
):
    checkpoint_config = SimpleCheckpointConfigurator("foo", empty_data_context).build()
    assert checkpoint_config.action_list == common_action_list


def test_simple_checkpoint_has_update_data_docs_action_that_should_update_all_sites_when_site_names_is_all(
    empty_data_context,
    store_validation_result_action,
    store_eval_parameter_action,
    update_data_docs_action,
):
    checkpoint_config = SimpleCheckpointConfigurator(
        "foo", empty_data_context, site_names="all"
    ).build()
    # This is confusing: the UpdateDataDocsAction default behavior is to update
    # all sites if site_names=None
    update_data_docs_action["action"]["site_names"] = []
    assert checkpoint_config.action_list == [
        store_validation_result_action,
        store_eval_parameter_action,
        update_data_docs_action,
    ]


def test_simple_checkpoint_raises_errors_on_invalid_site_name_types(
    empty_data_context,
):
    for junk_input in [[1, "local"], 1, ["local", None]]:
        with pytest.raises(TypeError):
            SimpleCheckpointConfigurator(
                "foo", empty_data_context, site_names=junk_input
            ).build()


def test_simple_checkpoint_raises_errors_on_site_name_that_does_not_exist_on_data_context(
    empty_data_context,
):
    # assert the fixture is adequate
    assert "prod" not in empty_data_context.get_site_names()
    with pytest.raises(TypeError):
        SimpleCheckpointConfigurator(
            "foo", empty_data_context, site_names=["prod"]
        ).build()


@pytest.mark.integration
def test_simple_checkpoint_has_update_data_docs_action_that_should_update_selected_sites_when_sites_are_selected(
    empty_data_context,
    store_validation_result_action,
    store_eval_parameter_action,
    update_data_docs_action,
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
):
    # assert the fixture is adequate
    assert "local_site" in empty_data_context.get_site_names()

    checkpoint_config = SimpleCheckpointConfigurator(
        "foo", empty_data_context, site_names=["local_site"]
    ).build()
    # This is confusing: the UpdateDataDocsAction default behavior is to update
    # all sites if site_names=None
    update_data_docs_action["action"]["site_names"] = ["local_site"]
    assert checkpoint_config.action_list == [
        store_validation_result_action,
        store_eval_parameter_action,
        update_data_docs_action,
    ]

    # assert the fixture is adequate
    assert (
        "local_site"
        in titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates.get_site_names()
    )

    checkpoint_from_store = titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates.get_checkpoint(
        "my_simple_checkpoint_with_site_names"
    )
    checkpoint_config = checkpoint_from_store.get_config(mode=ConfigOutputModes.DICT)
    assert checkpoint_config["action_list"] == [
        store_validation_result_action,
        store_eval_parameter_action,
        update_data_docs_action,
    ]


def test_simple_checkpoint_has_no_update_data_docs_action_when_site_names_is_none(
    empty_data_context,
    store_validation_result_action,
    store_eval_parameter_action,
):
    # assert the fixture is adequate
    assert "local_site" in empty_data_context.get_site_names()

    checkpoint_config = SimpleCheckpointConfigurator(
        name="foo", data_context=empty_data_context, site_names=None
    ).build()
    assert checkpoint_config.action_list == [
        store_validation_result_action,
        store_eval_parameter_action,
    ]


def test_simple_checkpoint_persisted_to_store(
    context_with_data_source_and_empty_suite,
    store_validation_result_action,
    store_eval_parameter_action,
    one_validation,
):
    assert context_with_data_source_and_empty_suite.list_checkpoints() == []
    initial_checkpoint_config = SimpleCheckpointConfigurator(
        "foo",
        context_with_data_source_and_empty_suite,
        site_names=None,
    ).build()
    # TODO this add_checkpoint will be user facing and it could be more
    #  ergonomic by accepting a Checkpoint maybe .add_checkpoint() should take a
    #  Checkpoint and there should be a .create_checkpoint() that accepts all
    #  the current parameters
    context_with_data_source_and_empty_suite.add_checkpoint(
        **initial_checkpoint_config.to_json_dict()
    )
    assert context_with_data_source_and_empty_suite.list_checkpoints() == ["foo"]
    checkpoint: SimpleCheckpoint = cast(
        SimpleCheckpoint,
        context_with_data_source_and_empty_suite.get_checkpoint(name="foo"),
    )
    assert isinstance(checkpoint, Checkpoint)
    assert isinstance(checkpoint.get_config(mode=ConfigOutputModes.DICT), dict)
    checkpoint_config: dict = checkpoint.get_config(
        mode=ConfigOutputModes.JSON_DICT, clean_nulls=False
    )
    assert checkpoint_config == {
        "action_list": [
            store_validation_result_action,
            store_eval_parameter_action,
        ],
        "batch_request": {},
        "class_name": "Checkpoint",
        "config_version": 1.0,
        "default_validation_id": None,
        "evaluation_parameters": {},
        "expectation_suite_ge_cloud_id": None,
        "expectation_suite_name": None,
        "ge_cloud_id": None,
        "module_name": "great_expectations.checkpoint",
        "name": "foo",
        "notify_on": None,
        "notify_with": None,
        "profilers": [],
        "run_name_template": None,
        "runtime_configuration": {},
        "site_names": None,
        "slack_webhook": None,
        "template_name": None,
        "validations": [],
    }
    result = checkpoint.run(validations=[one_validation])
    assert result.success


def test_simple_checkpoint_defaults_run_and_no_run_params_raises_checkpoint_error(
    context_with_data_source_and_empty_suite, simple_checkpoint_defaults
):
    with pytest.raises(gx_exceptions.CheckpointError) as cpe:
        # noinspection PyUnusedLocal
        simple_checkpoint_defaults.run()
    assert (
        'Checkpoint "foo" must be called with a validator or contain either a batch_request or validations.'
        in str(cpe.value)
    )


@pytest.mark.slow  # 1.10s
def test_simple_checkpoint_defaults_run_and_basic_run_params_without_persisting_checkpoint(
    context_with_data_source_and_empty_suite, simple_checkpoint_defaults, one_validation
):
    # verify Checkpoint is not persisted in the data context
    assert context_with_data_source_and_empty_suite.list_checkpoints() == []
    result = simple_checkpoint_defaults.run(
        run_name="bar",
        validations=[one_validation],
    )
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert result.list_expectation_suite_names() == ["one"]
    assert len(result.list_validation_results()) == 1
    assert result.success


@pytest.mark.slow  # 1.09s
def test_simple_checkpoint_runtime_kwargs_processing_site_names_only_without_persisting_checkpoint(
    context_with_data_source_and_empty_suite,
    common_action_list,
    simple_checkpoint_defaults,
    one_validation,
):
    # verify Checkpoint is not persisted in the data context
    assert context_with_data_source_and_empty_suite.list_checkpoints() == []

    expected_runtime_kwargs: dict = {
        "name": "foo",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "template_name": None,
        "run_name_template": None,
        "expectation_suite_name": None,
        "batch_request": None,
        "action_list": common_action_list,
        "evaluation_parameters": None,
        "runtime_configuration": {},
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                },
                "expectation_suite_name": "one",
            },
        ],
        "profilers": None,
    }

    result: CheckpointResult = simple_checkpoint_defaults.run(
        run_name="bar",
        validations=[one_validation],
        site_names=["local_site"],
    )
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert result.list_expectation_suite_names() == ["one"]
    assert len(result.list_validation_results()) == 1
    assert result.success

    substituted_runtime_config: dict = (
        simple_checkpoint_defaults.get_substituted_config(
            runtime_kwargs=expected_runtime_kwargs
        )
    )
    assert deep_filter_properties_iterable(
        properties=substituted_runtime_config,
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_runtime_kwargs,
        clean_falsy=True,
    )


@pytest.mark.slow  # 1.52s
def test_simple_checkpoint_runtime_kwargs_processing_slack_webhook_only_without_persisting_checkpoint(
    context_with_data_source_and_empty_suite,
    slack_notification_action,
    common_action_list,
    simple_checkpoint_defaults,
    one_validation,
):
    # verify Checkpoint is not persisted in the data context
    assert context_with_data_source_and_empty_suite.list_checkpoints() == []

    expected_runtime_kwargs: dict = {
        "name": "foo",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "template_name": None,
        "run_name_template": None,
        "expectation_suite_name": None,
        "batch_request": None,
        "action_list": common_action_list + [slack_notification_action],
        "evaluation_parameters": None,
        "runtime_configuration": {},
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                },
                "expectation_suite_name": "one",
            }
        ],
        "profilers": None,
    }

    result: CheckpointResult = simple_checkpoint_defaults.run(
        run_name="bar",
        validations=[one_validation],
        slack_webhook="https://hooks.slack.com/my_slack_webhook.geocities",
    )
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert result.list_expectation_suite_names() == ["one"]
    assert len(result.list_validation_results()) == 1
    assert result.success

    substituted_runtime_config: dict = (
        simple_checkpoint_defaults.get_substituted_config(
            runtime_kwargs=expected_runtime_kwargs
        )
    )
    assert deep_filter_properties_iterable(
        properties=substituted_runtime_config,
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_runtime_kwargs,
        clean_falsy=True,
    )


@pytest.mark.slow  # 1.11s
def test_simple_checkpoint_runtime_kwargs_processing_all_special_kwargs_without_persisting_checkpoint(
    context_with_data_source_and_empty_suite,
    slack_notification_action,
    common_action_list,
    simple_checkpoint_defaults,
    one_validation,
):
    # verify Checkpoint is not persisted in the data context
    assert context_with_data_source_and_empty_suite.list_checkpoints() == []

    expected_runtime_kwargs: dict = {
        "name": "foo",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "template_name": None,
        "run_name_template": None,
        "expectation_suite_name": None,
        "batch_request": None,
        "action_list": common_action_list + [slack_notification_action],
        "evaluation_parameters": None,
        "runtime_configuration": {},
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                },
                "expectation_suite_name": "one",
            }
        ],
        "profilers": None,
    }

    result: CheckpointResult = simple_checkpoint_defaults.run(
        run_name="bar",
        validations=[one_validation],
        site_names=["local_site"],
        notify_with=["local_site"],
        notify_on="failure",
        slack_webhook="https://hooks.slack.com/my_slack_webhook.geocities",
    )
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert result.list_expectation_suite_names() == ["one"]
    assert len(result.list_validation_results()) == 1
    assert result.success

    substituted_runtime_config: dict = (
        simple_checkpoint_defaults.get_substituted_config(
            runtime_kwargs=expected_runtime_kwargs
        )
    )
    assert deep_filter_properties_iterable(
        properties=substituted_runtime_config,
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_runtime_kwargs,
        clean_falsy=True,
    )


@pytest.mark.integration
@pytest.mark.slow  # 1.23s
def test_simple_checkpoint_runtime_kwargs_processing_all_kwargs(
    titanic_pandas_data_context_with_v013_datasource_stats_enabled_with_checkpoints_v1_with_templates,
    slack_notification_action,
    common_action_list,
    simple_checkpoint_defaults,
    one_validation,
    monkeypatch,
):
    monkeypatch.setenv("GE_ENVIRONMENT", "my_ge_environment")
    monkeypatch.setenv("MY_PARAM", "1")
    monkeypatch.setenv("VAR", "test")

    expected_runtime_kwargs: dict = {
        "name": "foo",
        "config_version": 1.0,
        "class_name": "Checkpoint",
        "module_name": "great_expectations.checkpoint",
        "template_name": "my_simple_template_checkpoint",
        "run_name_template": "my_runtime_run_name_template",
        "expectation_suite_name": "my_runtime_suite",
        "batch_request": {
            "data_connector_query": {
                "index": -1,
            },
        },
        "action_list": common_action_list + [slack_notification_action],
        "evaluation_parameters": {
            "aux_param_0": "1",
            "aux_param_1": "1 + 1",
            "environment": "my_ge_environment",
            "my_runtime_key": "my_runtime_value",
            "tolerance": 0.01,
        },
        "runtime_configuration": {
            "my_runtime_key": "my_runtime_value",
            "result_format": {
                "result_format": "BASIC",
                "partial_unexpected_count": 20,
            },
        },
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "my_datasource",
                    "data_connector_name": "my_special_data_connector",
                    "data_asset_name": "users",
                },
                "expectation_suite_name": "one",
            }
        ],
        "profilers": None,
    }

    result: CheckpointResult = simple_checkpoint_defaults.run(
        run_name="bar",
        template_name="my_simple_template_checkpoint",
        run_name_template="my_runtime_run_name_template",
        expectation_suite_name="my_runtime_suite",
        batch_request={
            "data_connector_query": {
                "index": -1,
            },
        },
        validations=[one_validation],
        evaluation_parameters={"my_runtime_key": "my_runtime_value"},
        runtime_configuration={"my_runtime_key": "my_runtime_value"},
        site_names=["local_site"],
        notify_with=["local_site"],
        notify_on="failure",
        slack_webhook="https://hooks.slack.com/my_slack_webhook.geocities",
    )
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert result.list_expectation_suite_names() == ["one"]
    assert len(result.list_validation_results()) == 1
    assert result.success

    substituted_runtime_config: dict = (
        simple_checkpoint_defaults.get_substituted_config(
            runtime_kwargs=expected_runtime_kwargs
        )
    )
    assert deep_filter_properties_iterable(
        properties=substituted_runtime_config,
        clean_falsy=True,
    ) == deep_filter_properties_iterable(
        properties=expected_runtime_kwargs,
        clean_falsy=True,
    )


@pytest.mark.integration
@pytest.mark.slow  # 1.50s
def test_simple_checkpoint_defaults_run_and_basic_run_params_with_persisted_checkpoint_loaded_from_store(
    context_with_data_source_and_empty_suite,
    simple_checkpoint_defaults,
    webhook,
    one_validation,
):
    context: FileDataContext = context_with_data_source_and_empty_suite
    checkpoint_config = SimpleCheckpointConfigurator(
        "foo", context_with_data_source_and_empty_suite, slack_webhook=webhook
    ).build()
    context.add_checkpoint(**checkpoint_config.to_json_dict())
    checkpoint_name = checkpoint_config.name
    assert context.list_checkpoints() == [checkpoint_name]

    del checkpoint_config
    checkpoint: Union[Checkpoint, LegacyCheckpoint] = context.get_checkpoint(
        checkpoint_name
    )
    assert isinstance(checkpoint, Checkpoint)

    result = checkpoint.run(run_name="bar", validations=[one_validation])
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert result.list_expectation_suite_names() == ["one"]
    assert len(result.list_validation_results()) == 1
    assert result.success


@pytest.mark.slow  # 1.12s
def test_simple_checkpoint_defaults_run_with_top_level_batch_request_and_suite(
    context_with_data_source_and_empty_suite, simple_checkpoint_defaults
):
    result = simple_checkpoint_defaults.run(
        run_name="bar",
        batch_request={
            "datasource_name": "my_datasource",
            "data_connector_name": "my_special_data_connector",
            "data_asset_name": "users",
        },
        expectation_suite_name="one",
        validations=[{"expectation_suite_name": "one"}],
    )
    assert isinstance(result, CheckpointResult)
    assert result.success
    assert len(result.run_results) == 1


def test_simple_checkpoint_error_with_invalid_top_level_batch_request(
    simple_checkpoint_defaults,
):
    # raised by _validate_init_parameters() in BatchRequest.__init__()
    with pytest.raises(TypeError):
        # missing data_asset_name
        simple_checkpoint_defaults.run(
            run_name="bar",
            batch_request={
                "datasource_name": "my_datasource",
                "data_connector_name": "my_special_data_connector",
            },
            expectation_suite_name="one",
            validations=[{"expectation_suite_name": "one"}],
        )


@pytest.mark.integration
@pytest.mark.slow  # 1.61s
def test_simple_checkpoint_defaults_run_multiple_validations_without_persistence(
    context_with_data_source_and_empty_suite,
    simple_checkpoint_defaults,
    two_validations,
):
    context_with_data_source_and_empty_suite.add_expectation_suite("two")
    assert len(context_with_data_source_and_empty_suite.list_expectation_suites()) == 2
    result = simple_checkpoint_defaults.run(
        run_name="bar",
        validations=two_validations,
    )
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert sorted(result.list_expectation_suite_names()) == sorted(["one", "two"])
    assert len(result.list_validation_results()) == 2
    assert result.success


@pytest.mark.integration
@pytest.mark.slow  # 1.62s
def test_simple_checkpoint_defaults_run_multiple_validations_with_persisted_checkpoint_loaded_from_store(
    context_with_data_source_and_empty_suite,
    simple_checkpoint_defaults,
    two_validations,
):
    context: FileDataContext = context_with_data_source_and_empty_suite
    context.add_expectation_suite("two")
    assert len(context.list_expectation_suites()) == 2

    # persist to store
    checkpoint_class_args: dict = simple_checkpoint_defaults.get_config(
        mode=ConfigOutputModes.JSON_DICT
    )
    context.add_checkpoint(**checkpoint_class_args)
    checkpoint_name = simple_checkpoint_defaults.name
    assert context.list_checkpoints() == [checkpoint_name]
    # reload from store
    del simple_checkpoint_defaults
    checkpoint: Union[Checkpoint, LegacyCheckpoint] = context.get_checkpoint(
        checkpoint_name
    )
    result = checkpoint.run(run_name="bar", validations=two_validations)
    assert isinstance(result, CheckpointResult)
    assert result.run_id.run_name == "bar"
    assert sorted(result.list_expectation_suite_names()) == sorted(["one", "two"])
    assert len(result.list_validation_results()) == 2
    assert result.success


@pytest.mark.integration
def test_simple_checkpoint_with_runtime_batch_request_and_runtime_data_connector_creates_config(
    context_with_data_source_and_empty_suite,
    common_action_list,
):
    context: FileDataContext = context_with_data_source_and_empty_suite
    runtime_batch_request = RuntimeBatchRequest(
        datasource_name="my_datasource",
        data_connector_name="my_runtime_data_connector",
        data_asset_name="users",
        batch_identifiers={"pipeline_stage_name": "first"},  # defined in fixture
        runtime_parameters={
            "query": "SELECT * FROM taxi_data"
        },  # not actually run, but used to test configuration
    )

    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint", data_context=context, batch_request=runtime_batch_request
    )
    checkpoint_config: dict = checkpoint.get_config(mode=ConfigOutputModes.JSON_DICT)

    assert isinstance(checkpoint_config, dict)
    assert checkpoint_config["name"] == "my_checkpoint"
    assert checkpoint_config["action_list"] == common_action_list
    assert deep_filter_properties_iterable(
        properties=checkpoint_config["batch_request"],
        clean_falsy=True,
    ) == {
        "batch_identifiers": {"pipeline_stage_name": "first"},
        "data_asset_name": "users",
        "data_connector_name": "my_runtime_data_connector",
        "datasource_name": "my_datasource",
        "runtime_parameters": {"query": "SELECT * FROM taxi_data"},
    }
    assert checkpoint_config["config_version"] == 1.0
    assert checkpoint_config["evaluation_parameters"] == {}
    assert checkpoint_config["runtime_configuration"] == {}
    assert checkpoint_config["validations"] == []


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_single_runtime_batch_request_batch_data_in_validations_pandas(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_single_runtime_batch_request_batch_data_in_validations_spark(
    data_context_with_datasource_spark_engine, common_action_list, spark_session
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_single_runtime_batch_request_query_in_validations(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        validations=[{"batch_request": batch_request}],
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_multiple_runtime_batch_request_query_in_validations(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
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

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
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
def test_simple_checkpoint_raise_error_when_run_when_missing_batch_request_and_validations(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
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
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_query_in_top_level_batch_request(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        batch_request=batch_request,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_top_level_batch_request_pandas(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_top_level_batch_request_spark(
    data_context_with_datasource_spark_engine,
    common_action_list,
    spark_session,
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.08s
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_top_level_batch_request_pandas(
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
    batch_request = RuntimeBatchRequest(
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

    # add simple checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        batch_request=batch_request,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_top_level_batch_request_spark(
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
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
        batch_request=batch_request,
    )

    result = checkpoint.run()

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_query_in_checkpoint_run(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_checkpoint_run_pandas(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_checkpoint_run_spark(
    data_context_with_datasource_spark_engine, common_action_list, spark_session
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_query_in_checkpoint_run(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_batch_data_in_checkpoint_run_pandas(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_batch_data_in_checkpoint_run_spark(
    data_context_with_datasource_spark_engine, common_action_list, spark_session
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.06s
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_checkpoint_run_pandas(
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
    batch_request = RuntimeBatchRequest(
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

    # add simple checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_checkpoint_run_spark(
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
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.07s
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_path_checkpoint_run_pandas(
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
    batch_request = RuntimeBatchRequest(
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

    # add simple checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_path_in_checkpoint_run_spark(
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
    batch_request = RuntimeBatchRequest(
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
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(validations=[{"batch_request": batch_request}])

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_query_in_context_run_checkpoint(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
    checkpoint_config_dict: dict = {
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config_dict)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_context_run_checkpoint_pandas(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_batch_data_in_context_run_checkpoint_spark(
    data_context_with_datasource_spark_engine, common_action_list, spark_session
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_query_in_context_run_checkpoint(
    data_context_with_datasource_sqlalchemy_engine,
    common_action_list,
    sa,
):
    context: FileDataContext = data_context_with_datasource_sqlalchemy_engine

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", validations=[{"batch_request": batch_request}]
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_batch_data_in_context_run_checkpoint_pandas(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", validations=[{"batch_request": batch_request}]
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_batch_data_in_context_run_checkpoint_spark(
    data_context_with_datasource_spark_engine, common_action_list, spark_session
):
    context: FileDataContext = data_context_with_datasource_spark_engine
    pandas_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    test_df = spark_session.createDataFrame(pandas_df)

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", validations=[{"batch_request": batch_request}]
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.13s
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_context_run_checkpoint_pandas(
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
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_batch_request_path_in_context_run_checkpoint_spark(
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
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", batch_request=batch_request
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
@pytest.mark.slow  # 1.16s
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_path_context_run_checkpoint_pandas(
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
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", validations=[{"batch_request": batch_request}]
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_validation_result_when_run_runtime_validations_path_in_context_run_checkpoint_spark(
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
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
    }

    context.add_checkpoint(**checkpoint_config)

    result = context.run_checkpoint(
        checkpoint_name="my_checkpoint", validations=[{"batch_request": batch_request}]
    )

    assert len(context.validations_store.list_keys()) == 1
    assert result["success"]


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_printable_validation_result_with_batch_data(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
        **{
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "default_data_asset_name",
            "batch_identifiers": {"default_identifier_name": "test_identifier"},
            "runtime_parameters": {"batch_data": test_df},
        }
    )

    # add checkpoint config
    checkpoint: SimpleCheckpoint = SimpleCheckpoint(
        name="my_checkpoint",
        data_context=context,
        config_version=1,
        run_name_template="%Y-%M-foo-bar-template",
        expectation_suite_name="my_expectation_suite",
        action_list=common_action_list,
    )

    result = checkpoint.run(batch_request=batch_request)

    assert type(repr(result)) == str


@pytest.mark.integration
def test_simple_checkpoint_instantiates_and_produces_a_runtime_parameters_error_contradictory_batch_request_in_checkpoint_yml_and_checkpoint_run(
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

    runtime_batch_request: RuntimeBatchRequest

    # RuntimeBatchRequest with a path
    # Using typed object instead of dictionary, expected by "add_checkpoint()", on purpose to insure that checks work.
    runtime_batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": runtime_batch_request,
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Union[Checkpoint, LegacyCheckpoint] = context.get_checkpoint(
        name="my_checkpoint"
    )

    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    runtime_batch_request = RuntimeBatchRequest(
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


@pytest.mark.integration
@pytest.mark.slow  # 1.73s
def test_simple_checkpoint_instantiates_and_produces_a_correct_validation_result_batch_request_in_checkpoint_yml_and_checkpoint_run(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "batch_request": batch_request,
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Union[Checkpoint, LegacyCheckpoint] = context.get_checkpoint(
        name="my_checkpoint"
    )

    result = checkpoint.run()
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


@pytest.mark.integration
@pytest.mark.slow  # 2.32s
def test_simple_checkpoint_instantiates_and_produces_a_correct_validation_result_validations_in_checkpoint_yml_and_checkpoint_run(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [{"batch_request": batch_request}],
    }

    context.add_checkpoint(**checkpoint_config)
    checkpoint: Union[Checkpoint, LegacyCheckpoint] = context.get_checkpoint(
        name="my_checkpoint"
    )

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


@pytest.mark.integration
@pytest.mark.slow  # 1.87s
def test_simple_checkpoint_instantiates_and_produces_a_correct_validation_result_batch_request_in_checkpoint_yml_and_context_run_checkpoint(
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
        "class_name": "SimpleCheckpoint",
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


@pytest.mark.integration
@pytest.mark.slow  # 2.44s
def test_simple_checkpoint_instantiates_and_produces_a_correct_validation_result_validations_in_checkpoint_yml_and_context_run_checkpoint(
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
        "class_name": "SimpleCheckpoint",
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
def test_simple_checkpoint_does_not_pass_dataframes_via_batch_request_into_checkpoint_store(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
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
def test_simple_checkpoint_does_not_pass_dataframes_via_validations_into_checkpoint_store(
    data_context_with_datasource_pandas_engine,
    common_action_list,
):
    context: FileDataContext = data_context_with_datasource_pandas_engine
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # create expectation suite
    context.add_expectation_suite("my_expectation_suite")

    # RuntimeBatchRequest with a query
    batch_request = RuntimeBatchRequest(
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
        "class_name": "SimpleCheckpoint",
        "name": "my_checkpoint",
        "config_version": 1,
        "run_name_template": "%Y-%M-foo-bar-template",
        "expectation_suite_name": "my_expectation_suite",
        "action_list": common_action_list,
        "validations": [{"batch_request": batch_request}],
    }

    with pytest.raises(
        gx_exceptions.InvalidConfigError,
        match='batch_data found in validations cannot be saved to CheckpointStore "checkpoint_store"',
    ):
        context.add_checkpoint(**checkpoint_config)


@pytest.mark.integration
@pytest.mark.slow  # 1.16s
def test_simple_checkpoint_result_validations_include_rendered_content(
    titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation,
):
    context: FileDataContext = titanic_pandas_data_context_stats_enabled_and_expectation_suite_with_one_expectation

    batch_request: dict = {
        "datasource_name": "my_datasource",
        "data_connector_name": "my_basic_data_connector",
        "data_asset_name": "Titanic_1911",
    }

    expectation_suite_name = "my_expectation_suite"
    include_rendered_content = True

    # add checkpoint config
    checkpoint_config = {
        "class_name": "SimpleCheckpoint",
        "validations": [
            {
                "batch_request": batch_request,
                "expectation_suite_name": expectation_suite_name,
                "include_rendered_content": include_rendered_content,
            }
        ],
    }
    checkpoint = SimpleCheckpoint(
        name="my_checkpoint", data_context=context, **checkpoint_config
    )

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
def test_running_spark_simplecheckpoint(
    context_with_single_csv_spark_and_suite, spark_df_taxi_data_schema
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
        "name": "my_checkpoint",
        "config_version": 1,
        "class_name": "SimpleCheckpoint",
        "validations": [
            {
                "batch_request": single_batch_batch_request,
                "expectation_suite_name": "my_expectation_suite",
            }
        ],
    }
    context.add_checkpoint(**checkpoint_config)
    results = context.run_checkpoint(checkpoint_name="my_checkpoint")
    assert results.success is True


@pytest.mark.integration
def test_run_spark_checkpoint_with_schema(
    context_with_single_csv_spark_and_suite,
    update_data_docs_action,
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
        "name": "my_checkpoint",
        "config_version": 1,
        "class_name": "SimpleCheckpoint",
        "validations": [
            {
                "batch_request": single_batch_batch_request,
                "expectation_suite_name": "my_expectation_suite",
            }
        ],
        "action_list": [
            update_data_docs_action,
        ],
    }
    context.add_checkpoint(**checkpoint_config)
    results = context.run_checkpoint(checkpoint_name="my_checkpoint")

    assert results.success is True
