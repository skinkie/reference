from dataclasses import dataclass

from .spot_sensor_version_structure import SpotSensorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotSensor(SpotSensorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
