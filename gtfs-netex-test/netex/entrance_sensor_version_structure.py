from dataclasses import dataclass

from .sensor_equipment_version_structure import SensorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceSensorVersionStructure(SensorEquipmentVersionStructure):
    class Meta:
        name = "EntranceSensor_VersionStructure"
