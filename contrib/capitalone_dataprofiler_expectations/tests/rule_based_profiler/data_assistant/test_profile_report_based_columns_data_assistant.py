import os
import pytest
from typing import Dict, List, Optional, cast
from unittest import mock

from great_expectations import DataContext
from great_expectations.core import ExpectationSuite
from great_expectations.core.metric_domain_types import MetricDomainTypes
from great_expectations.core.usage_statistics.events import UsageStatsEvents
from great_expectations.rule_based_profiler.data_assistant_result import (
    DataAssistantResult,
)
from great_expectations.rule_based_profiler.domain import Domain
from great_expectations.rule_based_profiler.parameter_container import (
    FULLY_QUALIFIED_PARAMETER_NAME_ATTRIBUTED_VALUE_KEY,
    ParameterNode,
)
# noinspection PyUnresolvedReferences
import contrib.capitalone_dataprofiler_expectations.capitalone_dataprofiler_expectations.metrics.data_profiler_metrics
# noinspection PyUnresolvedReferences
from contrib.capitalone_dataprofiler_expectations.capitalone_dataprofiler_expectations.rule_based_profiler.data_assistant import (
    DataProfilerStructuredDataAssistant
)
from contrib.capitalone_dataprofiler_expectations.capitalone_dataprofiler_expectations.rule_based_profiler.data_assistant_result import (
    DataProfilerStructuredDataAssistantResult
)

# noinspection PyUnresolvedReferences
from tests.conftest import (
    bobby_columnar_table_multi_batch_probabilistic_data_context,
    bobby_columnar_table_multi_batch_deterministic_data_context,
    no_usage_stats,
    set_consistent_seed_within_numeric_metric_range_multi_batch_parameter_builder,
)


@pytest.fixture
def bobby_profile_report_based_columns_data_assistant_result_usage_stats_enabled(
        bobby_columnar_table_multi_batch_deterministic_data_context: DataContext,
) -> DataProfilerStructuredDataAssistantResult:
    context: DataContext = bobby_columnar_table_multi_batch_deterministic_data_context

    batch_request: dict = {
        "datasource_name": "taxi_pandas",
        "data_connector_name": "monthly",
        "data_asset_name": "my_reports",
        "data_connector_query": {"index": -1},
    }
    exclude_column_names = [
        "pickup_datetime",
        "dropoff_datetime",
        "store_and_fwd_flag",
        "congestion_surcharge",
    ]

    data_assistant_result: DataAssistantResult = context.assistants.data_profiler.run(
        batch_request=batch_request,
        columns_rule={
            "profile_path": os.path.join("/".join(os.getcwd().split("/")[:-2]),
                                         os.path.join(
                                             "data_profiler_files",
                                             "profile.pkl",
                                         )
                                         ),
        },
        exclude_column_names=exclude_column_names,
        estimation="flag_outliers",
    )

    return cast(DataProfilerStructuredDataAssistantResult, data_assistant_result)


@pytest.fixture(scope="module")
def bobby_profile_report_based_columns_data_assistant_result(
        bobby_columnar_table_multi_batch_probabilistic_data_context: DataContext,
) -> DataProfilerStructuredDataAssistantResult:
    context: DataContext = bobby_columnar_table_multi_batch_probabilistic_data_context

    batch_request: dict = {
        "datasource_name": "taxi_pandas",
        "data_connector_name": "monthly",
        "data_asset_name": "my_reports",
        "data_connector_query": {"index": -1},

    }

    exclude_column_names = [
        "pickup_datetime",
        "dropoff_datetime",
        "store_and_fwd_flag",
        "congestion_surcharge",
    ]

    data_assistant_result: DataAssistantResult = context.assistants.data_profiler.run(
        batch_request=batch_request,
        exclude_column_names=exclude_column_names,
        columns_rule={
            "profile_path": os.path.join("/".join(os.getcwd().split("/")[:-2]),
                                         os.path.join(
                                             "data_profiler_files",
                                             "profile.pkl",
                                         )
                                         ),
        },
        estimation="flag_outliers",
    )

    return cast(DataProfilerStructuredDataAssistantResult, data_assistant_result)

@pytest.mark.integration
@pytest.mark.slow  # 6.90s
def test_profile_report_based_columns_data_assistant_result_serialization(
        bobby_profile_report_based_columns_data_assistant_result: DataProfilerStructuredDataAssistantResult,
) -> None:
    profile_report_based_columns_data_assistant_result_as_dict: dict = (
        bobby_profile_report_based_columns_data_assistant_result.to_dict()
    )
    assert (
            set(profile_report_based_columns_data_assistant_result_as_dict.keys())
            == DataAssistantResult.ALLOWED_KEYS
    )
    assert (
            bobby_profile_report_based_columns_data_assistant_result.to_json_dict()
            == profile_report_based_columns_data_assistant_result_as_dict
    )
    assert len(bobby_profile_report_based_columns_data_assistant_result.profiler_config.rules) == 1


@pytest.mark.integration
@mock.patch(
    "great_expectations.core.usage_statistics.usage_statistics.UsageStatisticsHandler.emit"
)
@pytest.mark.slow  # 7.34s
def test_profile_report_based_columns_data_assistant_result_get_expectation_suite(
        mock_emit,
        bobby_profile_report_based_columns_data_assistant_result_usage_stats_enabled: DataProfilerStructuredDataAssistantResult,
):
    expectation_suite_name: str = "my_suite"

    suite: ExpectationSuite = bobby_profile_report_based_columns_data_assistant_result_usage_stats_enabled.get_expectation_suite(
        expectation_suite_name=expectation_suite_name
    )

    assert suite is not None and len(suite.expectations) > 0

    assert mock_emit.call_count == 1

    # noinspection PyUnresolvedReferences
    actual_events: List[unittest.mock._Call] = mock_emit.call_args_list
    assert (
            actual_events[-1][0][0]["event"]
            == UsageStatsEvents.DATA_ASSISTANT_RESULT_GET_EXPECTATION_SUITE.value
    )


@pytest.mark.integration
def test_profile_report_based_columns_data_assistant_metrics_count(
        bobby_profile_report_based_columns_data_assistant_result: DataProfilerStructuredDataAssistantResult,
) -> None:
    domain: Domain
    parameter_values_for_fully_qualified_parameter_names: Dict[str, ParameterNode]
    num_metrics: int

    domain_key = Domain(
        domain_type=MetricDomainTypes.TABLE,
    )

    num_metrics = 0
    for (
            domain,
            parameter_values_for_fully_qualified_parameter_names,
    ) in bobby_profile_report_based_columns_data_assistant_result.metrics_by_domain.items():
        if domain.is_superset(domain_key):
            num_metrics += len(parameter_values_for_fully_qualified_parameter_names)

    assert num_metrics == 0

    num_metrics = 0
    for (
            domain,
            parameter_values_for_fully_qualified_parameter_names,
    ) in bobby_profile_report_based_columns_data_assistant_result.metrics_by_domain.items():
        num_metrics += len(parameter_values_for_fully_qualified_parameter_names)

    assert num_metrics == 14


@pytest.mark.integration
def test_profile_report_based_columns_data_assistant_result_batch_id_to_batch_identifier_display_name_map_coverage(
        bobby_profile_report_based_columns_data_assistant_result: DataProfilerStructuredDataAssistantResult,
):
    metrics_by_domain: Optional[
        Dict[Domain, Dict[str, ParameterNode]]
    ] = bobby_profile_report_based_columns_data_assistant_result.metrics_by_domain

    parameter_values_for_fully_qualified_parameter_names: Dict[str, ParameterNode]
    parameter_node: ParameterNode
    batch_id: str
    assert all(
        bobby_profile_report_based_columns_data_assistant_result._batch_id_to_batch_identifier_display_name_map[
            batch_id
        ]
        is not None
        for parameter_values_for_fully_qualified_parameter_names in metrics_by_domain.values()
        for parameter_node in parameter_values_for_fully_qualified_parameter_names.values()
        for batch_id in (
            parameter_node[FULLY_QUALIFIED_PARAMETER_NAME_ATTRIBUTED_VALUE_KEY]
            if FULLY_QUALIFIED_PARAMETER_NAME_ATTRIBUTED_VALUE_KEY in parameter_node
            else {}
        ).keys()
    )
