from dataclasses import dataclass
from .equipment_place_version_structure import EquipmentPlaceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPlace(EquipmentPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
