from dataclasses import dataclass

from .production_timetable_capabilities_response_structure import ProductionTimetableCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableCapabilitiesResponse(ProductionTimetableCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
