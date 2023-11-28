from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.interchange_rule_filter import InterchangeRuleFilter

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRuleFiltersRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of INTERCHANGE RULE FILTERs.
    """
    class Meta:
        name = "interchangeRuleFilters_RelStructure"

    interchange_rule_filter: List[InterchangeRuleFilter] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
