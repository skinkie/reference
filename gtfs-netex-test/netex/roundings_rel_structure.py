from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .rounding import Rounding

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoundingsRelStructure(FrameContainmentStructure):
    class Meta:
        name = "roundings_RelStructure"

    rounding: list[Rounding] = field(
        default_factory=list,
        metadata={
            "name": "Rounding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
