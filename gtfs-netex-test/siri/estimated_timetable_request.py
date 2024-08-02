from dataclasses import dataclass

from .estimated_timetable_request_structure import EstimatedTimetableRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableRequest(EstimatedTimetableRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
