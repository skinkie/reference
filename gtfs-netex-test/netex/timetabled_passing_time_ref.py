from dataclasses import dataclass
from netex.timetabled_passing_time_ref_structure import TimetabledPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetabledPassingTimeRef(TimetabledPassingTimeRefStructure):
    """
    Reference to a TIMETABLED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
