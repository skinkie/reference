from dataclasses import dataclass
from netex.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointRefStructure(TimingPointRefStructure):
    """
    Type for a reference to a SCHEDULED STOP POINT.
    """
