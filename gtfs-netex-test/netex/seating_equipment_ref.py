from dataclasses import dataclass

from .seating_equipment_ref_structure import SeatingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SeatingEquipmentRef(SeatingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
