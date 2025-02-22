from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .individual_traveller import IndividualTraveller

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class IndividualTravellersInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "individualTravellersInFrame_RelStructure"

    individual_traveller: list[IndividualTraveller] = field(
        default_factory=list,
        metadata={
            "name": "IndividualTraveller",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
