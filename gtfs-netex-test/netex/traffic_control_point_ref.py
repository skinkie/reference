from dataclasses import dataclass

from .traffic_control_point_ref_structure import TrafficControlPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrafficControlPointRef(TrafficControlPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
