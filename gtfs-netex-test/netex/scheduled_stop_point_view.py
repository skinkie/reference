from dataclasses import dataclass
from netex.scheduled_stop_point_derived_view_structure import ScheduledStopPointDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointView(ScheduledStopPointDerivedViewStructure):
    """Simplified view of SCHEDULED STOP POINT.

    Includes derived some propertries of a stop.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
