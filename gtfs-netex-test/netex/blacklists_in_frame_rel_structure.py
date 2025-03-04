from dataclasses import dataclass, field

from .blacklist import Blacklist
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BlacklistsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "blacklistsInFrame_RelStructure"

    blacklist: list[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
