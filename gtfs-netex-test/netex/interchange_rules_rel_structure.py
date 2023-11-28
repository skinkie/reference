from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.interchange_rule import InterchangeRule
from netex.interchange_rule_ref import InterchangeRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRulesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of INTERCHANGE RULEs.
    """
    class Meta:
        name = "interchangeRules_RelStructure"

    interchange_rule_ref_or_interchange_rule: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeRuleRef",
                    "type": InterchangeRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRule",
                    "type": InterchangeRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
