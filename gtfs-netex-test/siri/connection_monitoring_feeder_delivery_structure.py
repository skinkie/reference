from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .monitored_feeder_arrival import MonitoredFeederArrival
from .monitored_feeder_arrival_cancellation import MonitoredFeederArrivalCancellation

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringFeederDeliveryStructure(AbstractServiceDeliveryStructure):
    monitored_feeder_arrival: List[MonitoredFeederArrival] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredFeederArrival",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_feeder_arrival_cancellation: List[MonitoredFeederArrivalCancellation] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredFeederArrivalCancellation",
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
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
