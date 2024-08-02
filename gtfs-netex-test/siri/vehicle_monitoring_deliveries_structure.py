from dataclasses import dataclass, field
from typing import List

from .vehicle_monitoring_delivery import VehicleMonitoringDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringDeliveriesStructure:
    vehicle_monitoring_delivery: List[VehicleMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
