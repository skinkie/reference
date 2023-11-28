from dataclasses import dataclass, field
from netex.traffic_control_point_version_structure import TrafficControlPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrafficControlPoint(TrafficControlPointVersionStructure):
    """A POINT where the traffic flow can be influenced.

    Examples are: traffic lights (lanterns), barriers.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
