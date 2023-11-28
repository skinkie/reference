from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.interchange_rule import InterchangeRule

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRulesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of INTERCHANGE RULEs.
    """
    class Meta:
        name = "interchangeRulesInFrame_RelStructure"

    interchange_rule: List[InterchangeRule] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
