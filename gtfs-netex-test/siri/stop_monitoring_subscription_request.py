from dataclasses import dataclass

from .stop_monitoring_subscription_structure import StopMonitoringSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringSubscriptionRequest(StopMonitoringSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
