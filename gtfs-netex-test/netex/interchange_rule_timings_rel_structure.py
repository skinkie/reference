from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.interchange_rule_timing import InterchangeRuleTiming
from netex.interchange_rule_timing_ref import InterchangeRuleTimingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRuleTimingsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of INTERCHANGE RULE TIMINGs.
    """
    class Meta:
        name = "interchangeRuleTimings_RelStructure"

    interchange_rule_timing_ref_or_interchange_rule_timing: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeRuleTimingRef",
                    "type": InterchangeRuleTimingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleTiming",
                    "type": InterchangeRuleTiming,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
