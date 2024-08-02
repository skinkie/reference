from dataclasses import dataclass

from .connection_timetable_delivery_structure import ConnectionTimetableDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableDelivery(ConnectionTimetableDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
