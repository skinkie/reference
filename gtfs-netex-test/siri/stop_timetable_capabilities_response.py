from dataclasses import dataclass

from .stop_timetable_capabilities_response_structure import StopTimetableCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableCapabilitiesResponse(StopTimetableCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
