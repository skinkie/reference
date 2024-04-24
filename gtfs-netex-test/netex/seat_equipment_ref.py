from dataclasses import dataclass

from .seat_equipment_ref_structure import SeatEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatEquipmentRef(SeatEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
