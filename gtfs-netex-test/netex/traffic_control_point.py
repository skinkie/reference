from dataclasses import dataclass

from .traffic_control_point_version_structure import TrafficControlPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrafficControlPoint(TrafficControlPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
