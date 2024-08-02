from dataclasses import dataclass

from .stop_timetable_delivery_structure import StopTimetableDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableDelivery(StopTimetableDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
