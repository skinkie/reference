from dataclasses import dataclass

from .seat_equipment_version_structure import SeatEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SeatEquipment(SeatEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
