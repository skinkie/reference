from dataclasses import dataclass
from .ticketing_equipment_ref_structure import TicketingEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingEquipmentRef(TicketingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
