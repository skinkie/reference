from dataclasses import dataclass, field
from typing import List

from .facility_monitoring_delivery import FacilityMonitoringDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringDeliveriesStructure:
    facility_monitoring_delivery: List[FacilityMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
