from dataclasses import dataclass

from .dated_timetable_version_frame_structure import DatedTimetableVersionFrameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedTimetableVersionFrame(DatedTimetableVersionFrameStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
