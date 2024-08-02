from dataclasses import dataclass, field
from typing import List, Optional

from .accessibility_assessment_structure import AccessibilityAssessmentStructure
from .affected_connection_link_structure import AffectedConnectionLinkStructure
from .affected_facility_structure import AffectedFacilityStructure
from .affected_modes_structure import AffectedModesStructure
from .affected_operator_structure import AffectedOperatorStructure
from .affected_section_structure import AffectedSectionStructure
from .affected_stop_place_component_structure import AffectedStopPlaceComponentStructure
from .affected_stop_place_element_structure import AffectedStopPlaceElementStructure
from .direction_structure import DirectionStructure
from .extensions_1 import Extensions1
from .line_ref import LineRef
from .link_projection_structure import LinkProjectionStructure
from .location_structure import LocationStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .navigation_path_ref_structure import NavigationPathRefStructure
from .published_line_name import PublishedLineName
from .route_link_ref_structure import RouteLinkRefStructure
from .route_point_type_enumeration import RoutePointTypeEnumeration
from .route_ref_structure import RouteRefStructure
from .stop_place_ref_structure import StopPlaceRefStructure
from .stop_place_type_enumeration import StopPlaceTypeEnumeration
from .stop_point_ref import StopPointRef
from .stop_point_type_enumeration import StopPointTypeEnumeration
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedStopPointStructure:
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    private_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_type: Optional[StopPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPointType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_modes: Optional[AffectedModesStructure] = field(
        default=None,
        metadata={
            "name": "AffectedModes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_condition: List[RoutePointTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StopCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_links: Optional["AffectedStopPointStructure.ConnectionLinks"] = field(
        default=None,
        metadata={
            "name": "ConnectionLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["AffectedStopPointStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
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

    @dataclass(kw_only=True)
    class ConnectionLinks:
        affected_connection_link: List[AffectedConnectionLinkStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedConnectionLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Lines:
        affected_line: List["AffectedLineStructure"] = field(
            default_factory=list,
            metadata={
                "name": "AffectedLine",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class AffectedRouteStructure:
    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction: List[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sections: Optional["AffectedRouteStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectedRouteStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_links: Optional["AffectedRouteStructure.RouteLinks"] = field(
        default=None,
        metadata={
            "name": "RouteLinks",
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

    @dataclass(kw_only=True)
    class Sections:
        affected_section: List[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class StopPoints:
        affected_only: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AffectedOnly",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        affected_stop_point: List[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
        link_projection_to_next_stop_point: List[LinkProjectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "LinkProjectionToNextStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class RouteLinks:
        route_link_ref: List[RouteLinkRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "RouteLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class AffectedLineStructure:
    affected_operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: LineRef = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    published_line_name: List[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origins: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origins",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destinations: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction: List[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    routes: Optional["AffectedLineStructure.Routes"] = field(
        default=None,
        metadata={
            "name": "Routes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sections: Optional["AffectedLineStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectedLineStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_places: Optional["AffectedLineStructure.StopPlaces"] = field(
        default=None,
        metadata={
            "name": "StopPlaces",
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

    @dataclass(kw_only=True)
    class Routes:
        affected_route: List[AffectedRouteStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedRoute",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Sections:
        affected_section: List[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class StopPoints:
        affected_stop_point: List[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class StopPlaces:
        affected_stop_place: List["AffectedStopPlaceStructure"] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class AffectedStopPlaceStructure(AffectedStopPlaceElementStructure):
    stop_place_ref: StopPlaceRefStructure = field(
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_type: Optional[StopPlaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_facilities: Optional["AffectedStopPlaceStructure.AffectedFacilities"] = field(
        default=None,
        metadata={
            "name": "AffectedFacilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_components: Optional["AffectedStopPlaceStructure.AffectedComponents"] = field(
        default=None,
        metadata={
            "name": "AffectedComponents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_navigation_paths: Optional["AffectedStopPlaceStructure.AffectedNavigationPaths"] = field(
        default=None,
        metadata={
            "name": "AffectedNavigationPaths",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["AffectedStopPlaceStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
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

    @dataclass(kw_only=True)
    class AffectedFacilities:
        affected_facility: List[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class AffectedComponents:
        affected_component: List[AffectedStopPlaceComponentStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedComponent",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class AffectedNavigationPaths:
        navigation_path_ref: List[NavigationPathRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "NavigationPathRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Lines:
        affected_line: List[AffectedLineStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedLine",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
