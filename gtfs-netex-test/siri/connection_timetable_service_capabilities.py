from dataclasses import dataclass

from .connection_timetable_service_capabilities_structure import ConnectionTimetableServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableServiceCapabilities(ConnectionTimetableServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
