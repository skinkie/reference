from dataclasses import dataclass
from netex.ticketing_equipment_ref_structure import TicketingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingEquipmentRef(TicketingEquipmentRefStructure):
    """
    Identifier of a TICKETING EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
