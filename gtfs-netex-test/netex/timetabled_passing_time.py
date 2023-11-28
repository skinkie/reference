from dataclasses import dataclass
from netex.timetabled_passing_time_versioned_child_structure import TimetabledPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetabledPassingTime(TimetabledPassingTimeVersionedChildStructure):
    """
    TIMETABLED PASSING TIME at TIMING POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
