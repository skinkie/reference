from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.rounding import Rounding

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundingsRelStructure(FrameContainmentStructure):
    """
    Set of FARE ROUNDING parameters such as rounding steps.
    """
    class Meta:
        name = "roundings_RelStructure"

    rounding: List[Rounding] = field(
        default_factory=list,
        metadata={
            "name": "Rounding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
