from dataclasses import dataclass

from .production_timetable_service_capabilities_structure import ProductionTimetableServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableServiceCapabilities(ProductionTimetableServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
