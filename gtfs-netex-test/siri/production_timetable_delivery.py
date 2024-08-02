from dataclasses import dataclass

from .production_timetable_delivery_structure import ProductionTimetableDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableDelivery(ProductionTimetableDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
