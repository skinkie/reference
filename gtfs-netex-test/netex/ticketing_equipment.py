from dataclasses import dataclass, field
from netex.ticketing_equipment_version_structure import TicketingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingEquipment(TicketingEquipmentVersionStructure):
    """
    Specialisation of PASSENGER EQUIPMENT for ticketing.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
