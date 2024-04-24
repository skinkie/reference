from dataclasses import dataclass

from .installed_equipment_version_structure import InstalledEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorEquipmentAbstract(InstalledEquipmentVersionStructure):
    class Meta:
        name = "SensorEquipment_"
        namespace = "http://www.netex.org.uk/netex"
