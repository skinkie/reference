from dataclasses import dataclass
from netex.timetabled_passing_time_view_structure import TimetabledPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetabledPassingTimeView(TimetabledPassingTimeViewStructure):
    """
    Simplified TIMETABLED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
