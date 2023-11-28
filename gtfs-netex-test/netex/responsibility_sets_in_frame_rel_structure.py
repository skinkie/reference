from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.responsibility_set import ResponsibilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of RESPONSIBILITY SETs.
    """
    class Meta:
        name = "responsibilitySetsInFrame_RelStructure"

    responsibility_set: List[ResponsibilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
