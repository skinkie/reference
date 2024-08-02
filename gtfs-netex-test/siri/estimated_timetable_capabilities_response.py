from dataclasses import dataclass

from .estimated_timetable_capabilities_response_structure import EstimatedTimetableCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableCapabilitiesResponse(EstimatedTimetableCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
