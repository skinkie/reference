from dataclasses import dataclass, field
from typing import Optional

from .entrance_ref_structure import EntranceRefStructure
from .level_ref_structure import LevelRefStructure
from .place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkEndStructure:
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
        },
    )
    entrance_ref: Optional[EntranceRefStructure] = field(
        default=None,
        metadata={
            "name": "EntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
