from dataclasses import dataclass, field
from netex.shelter_equipment_version_structure import ShelterEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ShelterEquipment(ShelterEquipmentVersionStructure):
    """
    Specialisation of WAITING EQUIPMENT for a SHELTER.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
