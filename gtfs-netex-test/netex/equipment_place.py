from dataclasses import dataclass, field
from netex.equipment_place_version_structure import EquipmentPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPlace(EquipmentPlaceVersionStructure):
    """
    Designated Place within a SITE for a locating EQUIPMENT.

    :ivar id: Identifier of  EQUIPMENT PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
