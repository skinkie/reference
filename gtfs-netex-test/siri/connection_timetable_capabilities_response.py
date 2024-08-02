from dataclasses import dataclass

from .connection_timetable_capabilities_response_structure import ConnectionTimetableCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableCapabilitiesResponse(ConnectionTimetableCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
