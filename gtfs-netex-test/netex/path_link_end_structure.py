from dataclasses import dataclass, field
from typing import Optional
from netex.entrance_ref_structure import EntranceRefStructure
from netex.level_ref_structure import LevelRefStructure
from netex.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkEndStructure:
    """
    Type for a PATH LINK ENd.

    :ivar place_ref: Reference to a PLACE, including QUAY, ACCESS SPACE,
        BOARDING POSITION or other node of a SITE.
    :ivar level_ref: Reference to a LEVEL on which SITE COMPONENT is
        found.
    :ivar entrance_ref: Reference to an ENTRANCE of a PLACE.
    """
    place_ref: PlaceRefStructure = field(
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    level_ref: Optional[LevelRefStructure] = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_ref: Optional[EntranceRefStructure] = field(
        default=None,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
