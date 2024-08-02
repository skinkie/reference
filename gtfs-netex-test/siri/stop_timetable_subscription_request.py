from dataclasses import dataclass

from .stop_timetable_subscription_structure import StopTimetableSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableSubscriptionRequest(StopTimetableSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
