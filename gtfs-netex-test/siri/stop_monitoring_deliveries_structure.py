from dataclasses import dataclass, field
from typing import List

from .stop_monitoring_delivery import StopMonitoringDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringDeliveriesStructure:
    stop_monitoring_delivery: List[StopMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
