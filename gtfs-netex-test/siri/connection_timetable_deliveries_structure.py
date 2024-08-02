from dataclasses import dataclass, field

from .connection_timetable_delivery import ConnectionTimetableDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableDeliveriesStructure:
    connection_timetable_delivery: ConnectionTimetableDelivery = field(
        metadata={
            "name": "ConnectionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
