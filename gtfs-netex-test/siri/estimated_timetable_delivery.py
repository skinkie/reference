from dataclasses import dataclass

from .estimated_timetable_delivery_structure import EstimatedTimetableDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableDelivery(EstimatedTimetableDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
