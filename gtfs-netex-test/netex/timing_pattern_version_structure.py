from dataclasses import dataclass, field
from typing import Optional
from netex.direction_type_enumeration import DirectionTypeEnumeration
from netex.route_ref_structure import RouteRefStructure
from netex.section_in_sequence_versioned_child_structure import LinkSequenceVersionStructure
from netex.time_demand_type_ref import TimeDemandTypeRef
from netex.timeband_ref import TimebandRef
from netex.timing_links_rel_structure import TimingLinksRelStructure
from netex.timing_points_in_journey_pattern_rel_structure import TimingPointsInJourneyPatternRelStructure
from netex.timing_points_rel_structure import TimingPointsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPatternVersionStructure(LinkSequenceVersionStructure):
    """
    Type for TIMING PATTERN.

    :ivar route_ref: Route that TIMING PATTERN describes.
    :ivar direction_type:
    :ivar time_demand_type_ref_or_timeband_ref:
    :ivar points_in_sequence: Ordered List of points used in TIMING
        PATTERN. specific to TIMING PATTERN.
    :ivar points: List of points used in TIMING PATTERN. May also be
        defined elsewhere. Can be used to encapsulate TIMING PATTERN
        with its component POINTS.
    :ivar links: List of links used in TIMING PATTERN. May also be
        defined elsewhere. Can be used to encapsulate TIMING PATTERN
        with its component Link.s.
    """
    class Meta:
        name = "TimingPattern_VersionStructure"

    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref_or_timeband_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    points_in_sequence: Optional[TimingPointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points: Optional[TimingPointsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    links: Optional[TimingLinksRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
