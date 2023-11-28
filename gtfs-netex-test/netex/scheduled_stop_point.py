from dataclasses import dataclass, field
from netex.scheduled_stop_point_version_structure import ScheduledStopPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPoint(ScheduledStopPointVersionStructure):
    """A POINT where passengers can board or alight from vehicles.

    It is open, which hierarchical level such a point has. It can
    represent a single door (BoardingPosition) or a whole ZONE. The
    association to the physical model is done with STOP ASSIGNMENTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
