from dataclasses import dataclass

from .estimated_timetable_service_capabilities_structure import EstimatedTimetableServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableServiceCapabilities(EstimatedTimetableServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
