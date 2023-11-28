from dataclasses import dataclass, field
from typing import Optional
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_view import DestinationDisplayView
from netex.direction_ref import DirectionRef
from netex.direction_type_enumeration import DirectionTypeEnumeration
from netex.direction_view import DirectionView
from netex.journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from netex.journey_pattern_layovers_rel_structure import JourneyPatternLayoversRelStructure
from netex.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from netex.journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.operational_context_ref import OperationalContextRef
from netex.route_ref import RouteRef
from netex.route_view import RouteView
from netex.section_in_sequence_versioned_child_structure import LinkSequenceVersionStructure
from netex.service_links_in_journey_pattern_rel_structure import ServiceLinksInJourneyPatternRelStructure
from netex.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.timing_pattern_ref import TimingPatternRef
from netex.type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServicePatternVersionStructure(LinkSequenceVersionStructure):
    """
    Type for a SERVICE PATTERN.

    :ivar route_ref_or_route_view:
    :ivar direction_type: DIRECTION of JOURNEY PATTERN. Should be same
        as for ROUTE on which PATTERN is based.
    :ivar direction_ref_or_direction_view:
    :ivar destination_display_ref_or_destination_display_view:
    :ivar type_of_journey_pattern_ref:
    :ivar operational_context_ref:
    :ivar timing_pattern_ref: Reference to a TIMING PATTERN.
    :ivar notice_assignments: Notices for JOURNEY PATTERN Points may be
    :ivar run_times: Ordered run times for JOURNEY PATTERN, specific to
        a TIME DEMAND TYPE.
    :ivar wait_times: WAIT TIMEs for JOURNEY PATTERN, specific to a TIME
        DEMAND TYPE.
    :ivar headways: Wait times for TIMING POINT. There may be different
        times for different time demands.
    :ivar layovers: Layovers associated with JOURNEY PATTERN.
    :ivar journey_patterns: JOURNEY PATTERNs that make up SERVICE
        PATTERN.
    :ivar points_in_sequence: Ordered collection of POINTs making up the
        SERVICE PATTERN.
    :ivar links_in_sequence: Ordered collection of LINKS  making up the
        SERVICE PATTERN.
    """
    class Meta:
        name = "ServicePattern_VersionStructure"

    route_ref_or_route_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteView",
                    "type": RouteView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    direction_ref_or_direction_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionView",
                    "type": DirectionView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    destination_display_ref_or_destination_display_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_times: Optional[JourneyPatternRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_times: Optional[JourneyPatternWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layovers: Optional[JourneyPatternLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_patterns: Optional[JourneyPatternRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_sequence: Optional[StopPointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    links_in_sequence: Optional[ServiceLinksInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "linksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
