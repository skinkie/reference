from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.individual_traveller import IndividualTraveller

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualTravellersInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of INDIVIDUAL TRAVELLERs.
    """
    class Meta:
        name = "individualTravellersInFrame_RelStructure"

    individual_traveller: List[IndividualTraveller] = field(
        default_factory=list,
        metadata={
            "name": "IndividualTraveller",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
