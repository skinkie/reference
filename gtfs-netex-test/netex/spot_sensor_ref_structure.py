from dataclasses import dataclass

from .sensor_equipment_ref_structure import SensorEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SpotSensorRefStructure(SensorEquipmentRefStructure):
    pass
