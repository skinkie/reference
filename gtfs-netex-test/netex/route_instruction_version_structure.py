from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.compass_bearing16_enumeration import CompassBearing16Enumeration
from netex.multilingual_string import MultilingualString
from netex.path_heading_enumeration import PathHeadingEnumeration
from netex.point_on_route_ref import PointOnRouteRef
from netex.simple_feature_ref import SimpleFeatureRef
from netex.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteInstructionVersionStructure(DataManagedObjectStructure):
    """
    Type for ROUTE a POINT.

    :ivar point_on_route_ref:
    :ivar instruction: Directions for following path step.
    :ivar path_heading: Relative heading for Instruction
    :ivar heading: Heading for Instructioni nternational boundary
        between two countries may be crossed.
    :ivar bearing: Compass Bearing for Instruction
    :ivar distance: Distance for step.
    :ivar transition: Transition for instruction.
    :ivar road_name: Directions for following path staep.
    :ivar simple_feature_ref:
    :ivar order: Relative order
    """
    class Meta:
        name = "RouteInstruction_VersionStructure"

    point_on_route_ref: Optional[PointOnRouteRef] = field(
        default=None,
        metadata={
            "name": "PointOnRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    instruction: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_heading: Optional[PathHeadingEnumeration] = field(
        default=None,
        metadata={
            "name": "PathHeading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    heading: Optional[CompassBearing16Enumeration] = field(
        default=None,
        metadata={
            "name": "Heading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    simple_feature_ref: Optional[SimpleFeatureRef] = field(
        default=None,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
