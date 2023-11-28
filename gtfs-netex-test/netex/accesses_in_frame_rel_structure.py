from dataclasses import dataclass, field
from typing import List
from netex.access import Access
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ACCESS.
    """
    class Meta:
        name = "accessesInFrame_RelStructure"

    access: List[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
