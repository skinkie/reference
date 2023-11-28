from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.garage import Garage

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GaragesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GARAGEs.
    """
    class Meta:
        name = "garagesInFrame_RelStructure"

    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
