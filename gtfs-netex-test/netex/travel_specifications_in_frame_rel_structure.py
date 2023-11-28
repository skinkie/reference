from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.travel_specification_1 import TravelSpecification1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelSpecificationsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of SALES TRANSACTIONs.
    """
    class Meta:
        name = "travelSpecificationsInFrame_RelStructure"

    travel_specification: List[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
