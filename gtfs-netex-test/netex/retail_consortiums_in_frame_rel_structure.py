from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.retail_consortium import RetailConsortium

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailConsortiumsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of  RETAIL CONSORTIUMs.
    """
    class Meta:
        name = "retailConsortiumsInFrame_RelStructure"

    retail_consortium: List[RetailConsortium] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortium",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
