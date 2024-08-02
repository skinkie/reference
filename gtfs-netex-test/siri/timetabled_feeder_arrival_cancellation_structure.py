from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_referencing_item_structure import AbstractReferencingItemStructure
from .branding_ref_structure import BrandingRefStructure
from .branding_structure import BrandingStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .interchange_ref_structure import InterchangeRefStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .line_ref_structure import LineRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .order import Order
from .published_line_name import PublishedLineName
from .route_ref_structure import RouteRefStructure
from .stop_point_name import StopPointName
from .stop_point_ref import StopPointRef
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .visit_number import VisitNumber

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetabledFeederArrivalCancellationStructure(AbstractReferencingItemStructure):
    interchange_ref: Optional[InterchangeRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: ConnectionLinkRefStructure = field(
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    visit_number: Optional[VisitNumber] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[Order] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: LineRefStructure = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    direction_ref: DirectionRefStructure = field(
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    vehicle_journey_ref: FramedVehicleJourneyRefStructure = field(
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_pattern_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: List[VehicleModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    published_line_name: List[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_of_lines_ref: Optional[GroupOfLinesRefStructure] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    branding_ref_or_branding: Optional[Union[BrandingRefStructure, BrandingStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BrandingRef",
                    "type": BrandingRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Branding",
                    "type": BrandingStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    reason: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
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
