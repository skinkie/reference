from dataclasses import dataclass

from .timetable_version_frame_structure import TimetableVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimetableFrame(TimetableVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
