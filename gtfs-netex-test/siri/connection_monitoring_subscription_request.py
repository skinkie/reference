from dataclasses import dataclass

from .connection_monitoring_subscription_request_structure import ConnectionMonitoringSubscriptionRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringSubscriptionRequest(ConnectionMonitoringSubscriptionRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
