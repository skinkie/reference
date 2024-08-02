from dataclasses import dataclass

from .stop_timetable_service_capabilities_structure import StopTimetableServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableServiceCapabilities(StopTimetableServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
