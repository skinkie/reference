from dataclasses import dataclass

from .connection_timetable_subscription_structure import ConnectionTimetableSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableSubscriptionRequest(ConnectionTimetableSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
