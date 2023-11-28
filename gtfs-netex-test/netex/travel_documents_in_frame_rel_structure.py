from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.travel_document import TravelDocument

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TRAVEL DOCUMENT.
    """
    class Meta:
        name = "travelDocumentsInFrame_RelStructure"

    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
