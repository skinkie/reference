from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .timetabled_stop_visit_cancellation_structure import TimetabledStopVisitCancellationStructure
from .timetabled_stop_visit_structure import TimetabledStopVisitStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableDeliveryStructure(AbstractServiceDeliveryStructure):
    timetabled_stop_visit: List[TimetabledStopVisitStructure] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledStopVisit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timetabled_stop_visit_cancellation: List[TimetabledStopVisitCancellationStructure] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledStopVisitCancellation",
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
