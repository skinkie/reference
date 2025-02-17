from dataclasses import dataclass

from .installed_equipment_version_structure import InstalledEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlaceEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "PlaceEquipment_VersionStructure"
