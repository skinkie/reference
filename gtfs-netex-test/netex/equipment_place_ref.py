from dataclasses import dataclass

from .equipment_place_ref_structure import EquipmentPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EquipmentPlaceRef(EquipmentPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
