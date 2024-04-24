from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .level_ref import LevelRef
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelInStructureVersionStructure(VersionedChildStructure):
    class Meta:
        name = "LevelInStructure_VersionStructure"

    floor_label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FloorLabel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    level_ref: LevelRef = field(
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
