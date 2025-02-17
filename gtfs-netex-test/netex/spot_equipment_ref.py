from dataclasses import dataclass

from .spot_equipment_ref_structure import SpotEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SpotEquipmentRef(SpotEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
