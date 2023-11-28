from dataclasses import dataclass
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointRef(ScheduledStopPointRefStructure):
    """
    Reference to a SCHEDULED STOP POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
