from dataclasses import dataclass

from .sensor_in_entrance_ref_structure import SensorInEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorInEntranceRef(SensorInEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
