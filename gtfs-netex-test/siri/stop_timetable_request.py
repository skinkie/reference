from dataclasses import dataclass

from .stop_timetable_request_structure import StopTimetableRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableRequest(StopTimetableRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
