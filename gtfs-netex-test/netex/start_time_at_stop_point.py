from dataclasses import dataclass
from netex.start_time_at_stop_point_versioned_child_structure import StartTimeAtStopPointVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StartTimeAtStopPoint(StartTimeAtStopPointVersionedChildStructure):
    """
    A time at which a Fare demand  time band ( peak, off peak, etc  ) is deemed to
    begin  or end for trips at a particular SCHEDULED STOP POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
