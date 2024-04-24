from dataclasses import dataclass

from .spot_equipment_ref_structure import SpotEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatEquipmentRefStructure(SpotEquipmentRefStructure):
    pass
