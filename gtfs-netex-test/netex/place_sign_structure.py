from dataclasses import dataclass, field
from typing import Optional

from .multilingual_string import MultilingualString
from .place_ref import PlaceRef
from .sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlaceSignStructure(SignEquipmentVersionStructure):
    place_name: MultilingualString = field(
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    place_ref: Optional[PlaceRef] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
