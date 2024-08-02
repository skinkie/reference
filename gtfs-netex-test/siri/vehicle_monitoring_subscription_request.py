from dataclasses import dataclass

from .vehicle_monitoring_subscription_structure import VehicleMonitoringSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringSubscriptionRequest(VehicleMonitoringSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
