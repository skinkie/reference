from dataclasses import dataclass, field
from typing import Optional
from netex.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.derived_view_structure import DerivedViewStructure
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_view import DestinationDisplayView
from netex.direction_ref import DirectionRef
from netex.direction_type_enumeration import DirectionTypeEnumeration
from netex.direction_view import DirectionView
from netex.journey_pattern_ref import JourneyPatternRef
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.operational_context_ref import OperationalContextRef
from netex.route_ref import RouteRef
from netex.route_view import RouteView
from netex.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.service_pattern_ref import ServicePatternRef
from netex.timing_pattern_ref import TimingPatternRef
from netex.type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternDerivedViewStructure(DerivedViewStructure):
    """
    Type for JOURNEY PATTERN VIEW.

    :ivar choice:
    :ivar route_ref_or_route_view:
    :ivar direction_type: DIRECTION of JOURNEY PATTERN. Should be same
        as for ROUTE on which PATTERN is based.
    :ivar direction_ref_or_direction_view:
    :ivar destination_display_ref_or_destination_display_view:
    :ivar type_of_journey_pattern_ref:
    :ivar operational_context_ref:
    :ivar timing_pattern_ref: Reference to a TIMING PATTERN.
    :ivar notice_assignments: Notices for JOURNEY PATTERN Points may be
    """
    class Meta:
        name = "JourneyPattern_DerivedViewStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
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
