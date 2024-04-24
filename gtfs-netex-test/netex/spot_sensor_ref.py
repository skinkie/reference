from dataclasses import dataclass

from .spot_sensor_ref_structure import SpotSensorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotSensorRef(SpotSensorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
