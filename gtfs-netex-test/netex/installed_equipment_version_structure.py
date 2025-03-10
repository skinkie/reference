from dataclasses import dataclass

from .equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InstalledEquipmentVersionStructure(EquipmentVersionStructure):
    class Meta:
        name = "InstalledEquipment_VersionStructure"
