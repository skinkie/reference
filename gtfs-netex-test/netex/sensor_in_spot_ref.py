from dataclasses import dataclass

from .sensor_in_spot_ref_structure import SensorInSpotRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorInSpotRef(SensorInSpotRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
