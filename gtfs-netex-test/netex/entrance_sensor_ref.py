from dataclasses import dataclass

from .entrance_sensor_ref_structure import EntranceSensorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceSensorRef(EntranceSensorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
