from dataclasses import dataclass, field

from .stop_timetable_delivery import StopTimetableDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableDeliveriesStructure:
    stop_timetable_delivery: StopTimetableDelivery = field(
        metadata={
            "name": "StopTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
