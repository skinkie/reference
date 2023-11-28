from dataclasses import dataclass
from netex.equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InstalledEquipmentVersionStructure(EquipmentVersionStructure):
    """
    Type for INSTALLED EQUIPMENT.
    """
    class Meta:
        name = "InstalledEquipment_VersionStructure"
