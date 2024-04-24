from dataclasses import dataclass

from .sensor_in_entrance_versioned_child_structure import SensorInEntranceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorInEntrance(SensorInEntranceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
