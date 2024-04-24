from dataclasses import dataclass

from .sensor_in_spot_versioned_child_structure import SensorInSpotVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorInSpot(SensorInSpotVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
