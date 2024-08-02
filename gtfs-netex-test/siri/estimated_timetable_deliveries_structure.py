from dataclasses import dataclass, field
from typing import List

from .estimated_timetable_delivery import EstimatedTimetableDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableDeliveriesStructure:
    estimated_timetable_delivery: List[EstimatedTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
