from dataclasses import dataclass, field
from netex.entrance_equipment_version_structure import EntranceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntranceEquipment(EntranceEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for ENTRANCEs (door, barrier,
    revolving door, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
