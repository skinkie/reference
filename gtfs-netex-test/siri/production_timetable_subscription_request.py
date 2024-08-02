from dataclasses import dataclass

from .production_timetable_subscription_structure import ProductionTimetableSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableSubscriptionRequest(ProductionTimetableSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
