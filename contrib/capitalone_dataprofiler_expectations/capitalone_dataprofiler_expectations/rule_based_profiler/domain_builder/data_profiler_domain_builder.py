from typing import Iterable, List, Optional, Union

from great_expectations.rule_based_profiler.parameter_container import (
    FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER,
)
from great_expectations.core.metric_domain_types import MetricDomainTypes
from great_expectations.rule_based_profiler.domain import Domain, SemanticDomainTypes
from great_expectations.rule_based_profiler.domain_builder import ColumnDomainBuilder
from great_expectations.rule_based_profiler.helpers.util import (
    build_domains_from_column_names,
)
from great_expectations.rule_based_profiler.parameter_container import (
    ParameterContainer,
)


class DataProfilerDomainBuilder(ColumnDomainBuilder):
    """
    This DomainBuilder uses column cardinality to identify domains.
    """

    def __init__(
        self,
        report: dict,
        domain_check_list: dict,
        include_column_names: Optional[Union[str, Optional[List[str]]]] = None,
        exclude_column_names: Optional[Union[str, Optional[List[str]]]] = None,
        include_column_name_suffixes: Optional[Union[str, Iterable, List[str]]] = None,
        exclude_column_name_suffixes: Optional[Union[str, Iterable, List[str]]] = None,
        semantic_type_filter_module_name: Optional[str] = None,
        semantic_type_filter_class_name: Optional[str] = None,
        include_semantic_types: Optional[
            Union[str, SemanticDomainTypes, List[Union[str, SemanticDomainTypes]]]
        ] = None,
        exclude_semantic_types: Optional[
            Union[str, SemanticDomainTypes, List[Union[str, SemanticDomainTypes]]]
        ] = None,
        data_context: Optional["BaseDataContext"] = None,  # noqa: F821
    ) -> None:
        """Create column domains where cardinality is within the specified limit.

        Cardinality refers to the number of unique values in a given domain.

        Limit mode can be absolute (number of unique values) or relative
        (proportion of unique values). You can choose one of: cardinality_limit_mode,
        max_unique_values or max_proportion_unique to specify the cardinality
        limit.
        Note that the limit must be met for each Batch separately.
        If other Batch objects contain additional columns, these will not be considered.

        Args:
            include_column_names: Explicitly specified desired columns (if None, it is computed based on active Batch).
            exclude_column_names: If provided, these columns are pre-filtered and excluded from consideration.
            include_column_name_suffixes: Explicitly specified desired suffixes for corresponding columns to match.
            exclude_column_name_suffixes: Explicitly specified desired suffixes for corresponding columns to not match.
            semantic_type_filter_module_name: module_name containing class that implements SemanticTypeFilter interfaces
            semantic_type_filter_class_name: class_name of class that implements SemanticTypeFilter interfaces
            include_semantic_types: single/multiple type specifications using SemanticDomainTypes (or str equivalents)
            to be included
            exclude_semantic_types: single/multiple type specifications using SemanticDomainTypes (or str equivalents)
            to be excluded
            data_context: BaseDataContext associated with this DomainBuilder
        """
        if exclude_column_names is None:
            exclude_column_names = [
                "id",
                "ID",
                "Id",
            ]

        if exclude_column_name_suffixes is None:
            exclude_column_name_suffixes = [
                "_id",
                "_ID",
            ]

        if exclude_semantic_types is None:
            exclude_semantic_types = [
                SemanticDomainTypes.BINARY,
                SemanticDomainTypes.CURRENCY,
                SemanticDomainTypes.IDENTIFIER,
            ]

        super().__init__(
            include_column_names=include_column_names,
            exclude_column_names=exclude_column_names,
            include_column_name_suffixes=include_column_name_suffixes,
            exclude_column_name_suffixes=exclude_column_name_suffixes,
            semantic_type_filter_module_name=semantic_type_filter_module_name,
            semantic_type_filter_class_name=semantic_type_filter_class_name,
            include_semantic_types=include_semantic_types,
            exclude_semantic_types=exclude_semantic_types,
            data_context=data_context,
        )
        self._report = report
        self._domain_check_list = domain_check_list

    @property
    def report(self) -> dict:
        return self._report

    @report.setter
    def report(self, value: Optional[dict]) -> None:
        self._report = value

    @property
    def domain_check_list(self) -> dict:
        return self._domain_check_list

    @property
    def domain_type(self) -> MetricDomainTypes:
        return MetricDomainTypes.COLUMN

    def get_effective_column_names(
        self,
    ) -> List[str]:
        column_names = []
        for column in self.report['data_stats']:
            column_name = column['column_name']
            for metric in self.domain_check_list['checks']:
                for key in metric['metric_name'].split(FULLY_QUALIFIED_PARAMETER_NAME_SEPARATOR_CHARACTER):
                    column = column.get(key)
                if column not in set(metric['accepted_values']):
                    column_name = None
            if column_name:
                column_names.append(column_name)
        return column_names

    def _get_domains(
        self,
        rule_name: str,
        variables: Optional[ParameterContainer] = None,
    ) -> List[Domain]:
        """Return domains matching the selected cardinality_limit_mode.

        Args:
            rule_name: name of Rule object, for which "Domain" objects are obtained.
            variables: Optional variables to substitute when evaluating.

        Returns:
            List of domains that match the desired cardinality.
        """
        effective_column_names: List[str] = self.get_effective_column_names()

        column_name: str
        domains: List[Domain] = build_domains_from_column_names(
            rule_name=rule_name,
            column_names=effective_column_names,
            domain_type=self.domain_type,
        )

        return domains
