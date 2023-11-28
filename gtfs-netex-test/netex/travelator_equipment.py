from dataclasses import dataclass, field
from netex.travelator_equipment_version_structure import TravelatorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelatorEquipment(TravelatorEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for TRAVELATORs (provides travelator
    attributes like speed, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
