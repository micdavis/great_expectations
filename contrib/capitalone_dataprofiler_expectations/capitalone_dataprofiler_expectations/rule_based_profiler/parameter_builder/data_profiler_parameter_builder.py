from typing import Dict, List, Optional, Union

import dataprofiler
import numpy as np

from great_expectations.rule_based_profiler.config import ParameterBuilderConfig
from great_expectations.rule_based_profiler.domain import Domain
from great_expectations.rule_based_profiler.helpers.util import (
    get_parameter_value_and_validate_return_type,
    sanitize_parameter_name,
)
from great_expectations.rule_based_profiler.metric_computation_result import (
    MetricComputationDetails,
    MetricComputationResult,
)
from great_expectations.rule_based_profiler.parameter_builder import ParameterBuilder
from great_expectations.rule_based_profiler.parameter_container import (
    FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER,
    FULLY_QUALIFIED_PARAMETER_NAME_ATTRIBUTED_VALUE_KEY,
    FULLY_QUALIFIED_PARAMETER_NAME_METADATA_KEY,
    FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY,
    ParameterContainer,
    DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
)
from great_expectations.types.attributes import Attributes


class DataProfilerParameterBuilder(ParameterBuilder):
    """
    A Single/Multi-Batch implementation for obtaining a resolved (evaluated) metric, using domain_kwargs, value_kwargs,
    and metric_name as arguments.
    """

    def __init__(
            self,
            name: str,
            metric_name: str,
            report: dict,
            metric_domain_kwargs: Optional[Union[str, dict]] = None,
            metric_value_kwargs: Optional[Union[str, dict]] = None,
            evaluation_parameter_builder_configs: Optional[
                List[ParameterBuilderConfig]
            ] = None,
            data_context: Optional["BaseDataContext"] = None,  # noqa: F821
    ) -> None:
        """
        Args:
            name: the name of this parameter -- this is user-specified parameter name (from configuration);
            it is not the fully-qualified parameter name; a fully-qualified parameter name must start with "$parameter."
            and may contain one or more subsequent parts (e.g., "$parameter.<my_param_from_config>.<metric_name>").
            metric_name: the name of a metric used in MetricConfiguration (must be a supported and registered metric)
            metric_domain_kwargs: used in MetricConfiguration
            metric_value_kwargs: used in MetricConfiguration
            single_batch_mode: Facilitates "MetricSingleBatchParameterBuilder" subclasses in leveraging this class.
            enforce_numeric_metric: used in MetricConfiguration to insure that metric computations return numeric values
            replace_nan_with_zero: if False (default), then if the computed metric gives NaN, then exception is raised;
            otherwise, if True, then if the computed metric gives NaN, then it is converted to the 0.0 (float) value.
            reduce_scalar_metric: if True (default), then reduces computation of 1-dimensional metric to scalar value.
            evaluation_parameter_builder_configs: ParameterBuilder configurations, executing and making whose respective
            ParameterBuilder objects' outputs available (as fully-qualified parameter names) is pre-requisite.
            These "ParameterBuilder" configurations help build parameters needed for this "ParameterBuilder".
            data_context: BaseDataContext associated with this ParameterBuilder
        """
        super().__init__(
            name=name,
            evaluation_parameter_builder_configs=evaluation_parameter_builder_configs,
            data_context=data_context,
        )

        self._metric_name = metric_name
        self._metric_domain_kwargs = metric_domain_kwargs
        self._metric_value_kwargs = metric_value_kwargs

        self._report = report

    @property
    def metric_name(self) -> str:
        return self._metric_name

    @metric_name.setter
    def metric_name(self, value: str) -> None:
        self._metric_name = value

    @property
    def metric_domain_kwargs(self) -> Optional[Union[str, dict]]:
        return self._metric_domain_kwargs

    @property
    def metric_value_kwargs(self) -> Optional[Union[str, dict]]:
        return self._metric_value_kwargs

    @metric_value_kwargs.setter
    def metric_value_kwargs(self, value: Optional[Union[str, dict]]) -> None:
        self._metric_value_kwargs = value

    @property
    def report(self) -> Union[str, bool]:
        return self._report

    @report.setter
    def report(self, value: Optional[dict]) -> None:
        self._report = value

    def _build_parameters(
            self,
            domain: Domain,
            variables: Optional[ParameterContainer] = None,
            parameters: Optional[Dict[str, ParameterContainer]] = None,
            recompute_existing_parameter_values: bool = False,
    ) -> Attributes:
        """
        Builds ParameterContainer object that holds ParameterNode objects with attribute name-value pairs and details.

        Returns:
            Attributes object, containing computed parameter values and parameter computation details metadata.
        """
        # Obtain single_batch_mode from "rule state" (i.e., variables and parameters); from instance variable otherwise.
        metric_value = None
        schema = self.report.get("global_stats").get("profile_schema")
        metric_name_list = self.metric_name.split(FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER)
        if metric_name_list[0] == "column":
            column_id_list = schema.get(domain.get("domain_kwargs").get("column"))
            assert len(column_id_list) == 1
            column_id = column_id_list[0]
            column_report = self.report.get("data_stats")[column_id]
            for key in metric_name_list[1:]:
                column_report = column_report.get(key)
            metric_value = column_report

        return Attributes(
            {
                FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY: np.array([[metric_value]]),
                FULLY_QUALIFIED_PARAMETER_NAME_METADATA_KEY: self.metric_name,
            }
        )


def build_data_profiler_parameter_builder(
        metric_name: str,
        report: dict,
        metric_domain_kwargs: Optional[
            Union[str, dict]
        ] = DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
        metric_value_kwargs: Optional[Union[str, dict]] = None,
) -> DataProfilerParameterBuilder:
    """
    This method instantiates "MetricMultiBatchParameterBuilder" class with specific arguments for given purpose.
    """
    name: str = sanitize_parameter_name(name=metric_name)
    return DataProfilerParameterBuilder(
        name=name,
        metric_name=metric_name,
        report=report,
        metric_domain_kwargs=metric_domain_kwargs,
        metric_value_kwargs=metric_value_kwargs,
        evaluation_parameter_builder_configs=None,
        data_context=None,
    )
