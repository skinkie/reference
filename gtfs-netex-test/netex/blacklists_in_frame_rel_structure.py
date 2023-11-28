from dataclasses import dataclass, field
from typing import List
from netex.blacklist import Blacklist
from netex.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlacklistsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of BLACK LISTS.
    """
    class Meta:
        name = "blacklistsInFrame_RelStructure"

    blacklist: List[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
