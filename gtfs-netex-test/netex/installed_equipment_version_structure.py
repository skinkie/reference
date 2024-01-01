from dataclasses import dataclass
from .equipment_version_structure import EquipmentVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InstalledEquipmentVersionStructure(EquipmentVersionStructure):
    class Meta:
        name = "InstalledEquipment_VersionStructure"
