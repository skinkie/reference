from dataclasses import dataclass, field
from typing import Optional

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .extensions_1 import Extensions1
from .facility_monitoring_request import FacilityMonitoringRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringSubscriptionStructure(AbstractSubscriptionStructure):
    facility_monitoring_request: FacilityMonitoringRequest = field(
        metadata={
            "name": "FacilityMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
