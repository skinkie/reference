from dataclasses import dataclass

from .timetabled_passing_time_ref_structure import TimetabledPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimetabledPassingTimeRef(TimetabledPassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
