from dataclasses import dataclass

from .vehicle_monitoring_delivery_structure import VehicleMonitoringDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringDelivery(VehicleMonitoringDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
