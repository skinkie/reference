from dataclasses import dataclass
from netex.timetable_frame_ref_structure import TimetableFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetableFrameRef(TimetableFrameRefStructure):
    """
    Reference to a TIMETABLE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
