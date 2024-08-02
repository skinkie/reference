from dataclasses import dataclass

from .facility_monitoring_subscription_structure import FacilityMonitoringSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringSubscriptionRequest(FacilityMonitoringSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
