from dataclasses import dataclass

from .production_timetable_request_structure import ProductionTimetableRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableRequest(ProductionTimetableRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
