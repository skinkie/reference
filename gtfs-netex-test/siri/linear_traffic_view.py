from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .traffic_view_record import TrafficViewRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class LinearTrafficView:
    linear_predefined_location_reference: str = field(
        metadata={
            "name": "linearPredefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    traffic_view_record: List[TrafficViewRecord] = field(
        default_factory=list,
        metadata={
            "name": "trafficViewRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    linear_traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearTrafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
