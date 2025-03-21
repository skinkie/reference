from dataclasses import dataclass

from .equipment_place_version_structure import EquipmentPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EquipmentPlace(EquipmentPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
