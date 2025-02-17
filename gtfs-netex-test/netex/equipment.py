from dataclasses import dataclass

from .equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Equipment(EquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
