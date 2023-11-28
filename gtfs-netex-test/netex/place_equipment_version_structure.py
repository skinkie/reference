from dataclasses import dataclass
from netex.installed_equipment_version_structure import InstalledEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    """
    Type for a PLACE EQUIPMENT.
    """
    class Meta:
        name = "PlaceEquipment_VersionStructure"
