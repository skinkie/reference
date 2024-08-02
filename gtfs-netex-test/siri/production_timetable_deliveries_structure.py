from dataclasses import dataclass, field
from typing import List

from .production_timetable_delivery import ProductionTimetableDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableDeliveriesStructure:
    production_timetable_delivery: List[ProductionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
