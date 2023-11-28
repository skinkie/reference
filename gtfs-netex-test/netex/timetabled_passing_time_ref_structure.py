from dataclasses import dataclass
from netex.passing_time_ref_structure import PassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetabledPassingTimeRefStructure(PassingTimeRefStructure):
    """
    Type for a reference to a TIMETABLED PASSING TIME.
    """
