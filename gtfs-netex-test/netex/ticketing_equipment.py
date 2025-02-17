from dataclasses import dataclass

from .ticketing_equipment_version_structure import TicketingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TicketingEquipment(TicketingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
