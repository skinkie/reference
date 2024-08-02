from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure
from .vehicle_activity_cancellation_structure import VehicleActivityCancellationStructure
from .vehicle_activity_structure import VehicleActivityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringDeliveryStructure(AbstractServiceDeliveryStructure):
    vehicle_activity: List[VehicleActivityStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_activity_cancellation: List[VehicleActivityCancellationStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivityCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_activity_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivityNote",
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
