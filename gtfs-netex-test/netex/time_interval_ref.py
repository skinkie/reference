from dataclasses import dataclass
from netex.time_interval_ref_structure import TimeIntervalRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeIntervalRef(TimeIntervalRefStructure):
    """
    Reference to a TIME INTERVAL.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
