from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .extension_type import ExtensionType
from .linear_traffic_view import LinearTrafficView

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TrafficView:
    traffic_view_time: XmlDateTime = field(
        metadata={
            "name": "trafficViewTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    predefined_location_set_reference: str = field(
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    linear_traffic_view: List[LinearTrafficView] = field(
        default_factory=list,
        metadata={
            "name": "linearTrafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewExtension",
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
