from typing import Any, Dict, List, Optional

from contrib.experimental.great_expectations_experimental.rule_based_profiler.data_assistant_result import (
    StatisticsDataAssistantResult,
)
from great_expectations.rule_based_profiler.helpers.runtime_environment import (
    RuntimeEnvironmentDomainTypeDirectives,
    RuntimeEnvironmentVariablesDirectives,
)
from great_expectations.rule_based_profiler.expectation_configuration_builder import (
    DefaultExpectationConfigurationBuilder,
    ExpectationConfigurationBuilder,
)
from contrib.capitalone_dataprofiler_expectations.capitalone_dataprofiler_expectations.rule_based_profiler.parameter_builder.data_profiler_parameter_builder import (
    build_data_profiler_parameter_builder,
)
from contrib.capitalone_dataprofiler_expectations.capitalone_dataprofiler_expectations.rule_based_profiler.domain_builder.data_profiler_domain_builder import (
    DataProfilerDomainBuilder
)
from great_expectations.rule_based_profiler.config import ParameterBuilderConfig
from great_expectations.rule_based_profiler.data_assistant import DataAssistant
from great_expectations.rule_based_profiler.data_assistant_result import (
    DataAssistantResult,
)
from great_expectations.rule_based_profiler.domain import SemanticDomainTypes
from great_expectations.rule_based_profiler.parameter_builder import (
    ParameterBuilder,
)
from great_expectations.rule_based_profiler.parameter_container import (
    DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
    FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER,
    FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY,
    VARIABLES_KEY,
)
from great_expectations.rule_based_profiler.rule import Rule
from great_expectations.validator.validator import Validator


class DataProfilerDataAssistant(DataAssistant):
    """
    StatisticsDataAssistant provides metrics for dataset exploration purposes.

    Fundamentally, StatisticsDataAssistant is "OnboardingDataAssistant minus Expectations -- only Metrics", the intended
    usecase being obtaining description of data via metrics as well as comparing metrics between sub-sampeled datasets
    to determine the smallest dataset, whose statistics represent the overall data distribution sufficiantly adequately.
    """

    __alias__: str = "dataprofiler"

    def __init__(
            self,
            name: str,
            validator: Validator,
    ) -> None:
        self._report = None
        super().__init__(
            name=name,
            validator=validator,
        )

    @property
    def report(self) -> dict:
        return self._report

    @property
    def metrics_parameter_builders_by_domain(self) -> dict:
        return self._metrics_parameter_builders_by_domain

    def get_variables(self) -> Optional[Dict[str, Any]]:
        """
        Returns:
            Optional "variables" configuration attribute name/value pairs (overrides), commonly-used in Builder objects.
        """
        return None

    def get_rules(self) -> Optional[List[Rule]]:
        """
        Returns:
            Optional custom list of "Rule" objects implementing particular "DataAssistant" functionality.
        """
        numeric_columns_rule: Rule = self._build_numeric_columns_rule()

        return [
            numeric_columns_rule,
        ]

    def _build_data_assistant_result(
            self, data_assistant_result: DataAssistantResult
    ) -> DataAssistantResult:
        return StatisticsDataAssistantResult(
            _batch_id_to_batch_identifier_display_name_map=data_assistant_result._batch_id_to_batch_identifier_display_name_map,
            profiler_config=data_assistant_result.profiler_config,
            profiler_execution_time=data_assistant_result.profiler_execution_time,
            rule_domain_builder_execution_time=data_assistant_result.rule_domain_builder_execution_time,
            rule_execution_time=data_assistant_result.rule_execution_time,
            metrics_by_domain=data_assistant_result.metrics_by_domain,
            expectation_configurations=data_assistant_result.expectation_configurations,
            citation=data_assistant_result.citation,
            _usage_statistics_handler=data_assistant_result._usage_statistics_handler,
        )

    def run(
            self,
            variables: Optional[Dict[str, Any]] = None,
            rules: Optional[Dict[str, Dict[str, Any]]] = None,
            variables_directives_list: Optional[
                List[RuntimeEnvironmentVariablesDirectives]
            ] = None,
            domain_type_directives_list: Optional[
                List[RuntimeEnvironmentDomainTypeDirectives]
            ] = None,
    ) -> DataAssistantResult:
        self._report = domain_type_directives_list[0].directives.pop('report')
        for rule in self.profiler.rules:
            rule.domain_builder.report = self.report
            for parameter_builder in rule.parameter_builders:
                parameter_builder.report = self.report

        return super().run(variables_directives_list=variables_directives_list,
                           domain_type_directives_list=domain_type_directives_list)

    @staticmethod
    def _build_numeric_columns_rule() -> Rule:
        """
        This method builds "Rule" object focused on emitting "ExpectationConfiguration" objects for numeric columns.
        """

        # Step-1: Instantiate "ColumnDomainBuilder" for selecting numeric columns (but not "ID-type" columns).
        numeric_column_type_domain_builder = DataProfilerDomainBuilder(
            {},
            {
                "checks":
                    [
                        {"metric_name": "data_type",
                         "accepted_values":
                             ["float", "int"]
                         }
                    ]
            },
            include_column_names=None,
            exclude_column_names=None,
            include_column_name_suffixes=None,
            exclude_column_name_suffixes=[
                "_id",
                "_ID",
            ],
            semantic_type_filter_module_name=None,
            semantic_type_filter_class_name=None,
            include_semantic_types=[
                SemanticDomainTypes.NUMERIC,
            ],
            exclude_semantic_types=[
                SemanticDomainTypes.IDENTIFIER,
            ],
            data_context=None,
        )

        # Step-2: Declare "ParameterBuilder" for every metric of interest.
        dp_parameter_builder: ParameterBuilder = (
            build_data_profiler_parameter_builder(
                metric_name="column.statistics.min",
                report={},
                metric_value_kwargs=None,
            )
        )

        # Step-3: Declare "ParameterBuilder" configurations for all additional statistics needed.
        evaluation_parameter_builder_configs: Optional[List[ParameterBuilderConfig]]

        evaluation_parameter_builder_configs = [
            ParameterBuilderConfig(
                **dp_parameter_builder.to_json_dict()
            ),
        ]

        # Step-4: Instantiate and return "Rule" object, comprised of "variables", "domain_builder",
        # "parameter_builders", and "expectation_configuration_builders" components.

        variables: dict = {
            "mostly": 1.0,
            "strict_min": False,
            "strict_max": False,
            "quantiles": [
                0.25,
                0.5,
                0.75,
            ],
            "allow_relative_error": False,
            "false_positive_rate": 0.05,
            "estimator": "bootstrap",
            "n_resamples": 9999,
            "random_seed": None,
            "quantile_statistic_interpolation_method": "nearest",
            "quantile_bias_correction": False,
            "quantile_bias_std_error_ratio_threshold": None,
            "include_estimator_samples_histogram_in_details": False,
            "truncate_values": {
                "lower_bound": None,
                "upper_bound": None,
            },
            "round_decimals": 15,
        }
        parameter_builders: List[ParameterBuilder] = [
            dp_parameter_builder,
        ]
        column_min_values_range_parameter_builder_for_validations: ParameterBuilder = DataAssistant.commonly_used_parameter_builders.build_numeric_metric_range_multi_batch_parameter_builder(
            metric_name=None,
            metric_value_kwargs=None,
            evaluation_parameter_builder_configs=evaluation_parameter_builder_configs,
        )

        validation_parameter_builder_configs = [
            ParameterBuilderConfig(
                **column_min_values_range_parameter_builder_for_validations.to_json_dict(),
            ),
        ]
        expect_column_min_to_be_between_expectation_configuration_builder = DefaultExpectationConfigurationBuilder(
            expectation_type="expect_column_min_to_be_between",
            validation_parameter_builder_configs=validation_parameter_builder_configs,
            column=f"{DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME}{FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER}column",
            min_value=f"{column_min_values_range_parameter_builder_for_validations.json_serialized_fully_qualified_parameter_name}{FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER}{FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY}[0]",
            max_value=None,
            strict_min=f"{VARIABLES_KEY}strict_min",
            strict_max=None,
            meta=None,
        )

        expectation_configuration_builders: List[ExpectationConfigurationBuilder] = [
            expect_column_min_to_be_between_expectation_configuration_builder,
        ]
        rule = Rule(
            name="numeric_columns_rule",
            variables=variables,
            domain_builder=numeric_column_type_domain_builder,
            parameter_builders=parameter_builders,
            expectation_configuration_builders=expectation_configuration_builders,
        )

        return rule
