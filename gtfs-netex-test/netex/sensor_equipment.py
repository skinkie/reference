from dataclasses import dataclass

from .sensor_equipment_version_structure import SensorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorEquipment(SensorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
