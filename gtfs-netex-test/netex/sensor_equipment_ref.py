from dataclasses import dataclass

from .sensor_equipment_ref_structure import SensorEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorEquipmentRef(SensorEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
