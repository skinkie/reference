from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_discovery_request_structure import AbstractDiscoveryRequestStructure
from .bounding_box_structure import BoundingBoxStructure
from .extensions_1 import Extensions1
from .line_ref_structure import LineRefStructure
from .location_structure import LocationStructure
from .operator_ref_structure import OperatorRefStructure
from .stop_points_detail_enumeration import StopPointsDetailEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopPointsDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    bounding_box_or_circle_or_place_ref: Optional[Union[BoundingBoxStructure, LocationStructure, str]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BoundingBox",
                    "type": BoundingBoxStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Circle",
                    "type": LocationStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "PlaceRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points_detail_level: Optional[StopPointsDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPointsDetailLevel",
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
