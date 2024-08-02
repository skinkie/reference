from dataclasses import dataclass

from .stop_monitoring_delivery_structure import StopMonitoringDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringDelivery(StopMonitoringDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
