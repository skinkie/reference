from dataclasses import dataclass
from netex.traffic_control_point_ref_structure import TrafficControlPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrafficControlPointRef(TrafficControlPointRefStructure):
    """
    Reference to a TRAFFIC CONTROL POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
