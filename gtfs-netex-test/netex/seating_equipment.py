from dataclasses import dataclass

from .seating_equipment_version_structure import SeatingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SeatingEquipment(SeatingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
