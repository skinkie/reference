from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .distributor_departure_cancellation_structure import DistributorDepartureCancellationStructure
from .extensions_1 import Extensions1
from .stopping_position_changed_departure_structure import StoppingPositionChangedDepartureStructure
from .wait_prolonged_departure_structure import WaitProlongedDepartureStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringDistributorDeliveryStructure(AbstractServiceDeliveryStructure):
    wait_prolonged_departure: List[WaitProlongedDepartureStructure] = field(
        default_factory=list,
        metadata={
            "name": "WaitProlongedDeparture",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stopping_position_changed_departure: List[StoppingPositionChangedDepartureStructure] = field(
        default_factory=list,
        metadata={
            "name": "StoppingPositionChangedDeparture",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_departure_cancellation: List[DistributorDepartureCancellationStructure] = field(
        default_factory=list,
        metadata={
            "name": "DistributorDepartureCancellation",
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
