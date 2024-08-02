from dataclasses import dataclass

from .estimated_timetable_subscription_structure import EstimatedTimetableSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableSubscriptionRequest(EstimatedTimetableSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
