from dataclasses import dataclass

from .entrance_sensor_version_structure import EntranceSensorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceSensor(EntranceSensorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
