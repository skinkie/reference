from dataclasses import dataclass

from .connection_timetable_request_structure import ConnectionTimetableRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableRequest(ConnectionTimetableRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
