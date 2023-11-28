from dataclasses import dataclass, field
from netex.turnaround_time_limit_time_versioned_child_structure import TurnaroundTimeLimitTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TurnaroundTimeLimitTime(TurnaroundTimeLimitTimeVersionedChildStructure):
    """The maximum time for which a vehicle may be scheduled to wait at a
    particular TIMING POINT (often included in a TURN STATION) without being
    returned to a PARKING POINT.

    A minimum time for a vehicle to turn its direction may also be
    recorded. This may be superseded by a DEAD RUN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
