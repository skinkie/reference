from dataclasses import dataclass
from netex.fare_scheduled_stop_point_ref_structure import FareScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareScheduledStopPointRef(FareScheduledStopPointRefStructure):
    """
    Reference to a FARE SCHEDULED STOP POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
