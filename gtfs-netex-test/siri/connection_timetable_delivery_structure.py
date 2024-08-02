from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .timetabled_feeder_arrival import TimetabledFeederArrival
from .timetabled_feeder_arrival_cancellation import TimetabledFeederArrivalCancellation

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableDeliveryStructure(AbstractServiceDeliveryStructure):
    timetabled_feeder_arrival: List[TimetabledFeederArrival] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledFeederArrival",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timetabled_feeder_arrival_cancellation: List[TimetabledFeederArrivalCancellation] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledFeederArrivalCancellation",
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
