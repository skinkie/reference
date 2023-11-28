from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.booking_arrangements_structure import BookingArrangementsStructure
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_view import DestinationDisplayView
from netex.dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.flexible_point_properties import FlexiblePointProperties
from netex.journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from netex.journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from netex.request_method_type_enumeration import RequestMethodTypeEnumeration
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.service_link_ref_structure import ServiceLinkRefStructure
from netex.stop_use_enumeration import StopUseEnumeration
from netex.timing_link_ref_structure import TimingLinkRefStructure
from netex.vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPointInJourneyPatternVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    """
    Type for a STOP POINT IN JOURNEY PATTERN.

    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar onward_timing_link_ref: Onward link - used to disambiguate if
        there are multiple links from the same stop, e.g. as for
        cloverleaf route topology. If not given explicitly assume there
        is only one link that connects the two.
    :ivar is_wait_point: Whether point is a wait point.
    :ivar wait_time_or_wait_times:
    :ivar headways: Wait times for TIMING POINT. There may be different
        times for different time demands.
    :ivar onward_service_link_ref: Link that connects this to the next
        point. Allows to disambiguate if there are multiple SERVICE
        LINKs between two SERVICE POINTs.
    :ivar for_alighting: Whether alighting is allowed at the stop.
        Default is true.
    :ivar for_boarding: Whether boarding is allowed at the stop. Default
        is true.
    :ivar destination_display_ref_or_destination_display_view:
    :ivar vias: Destinations that the SERVICE goes via.
    :ivar flexible_point_properties:
    :ivar change_of_destination_display: Whether DESTINATION DISPLAY
        should be updated at this point. If DESTINATION NAME value is
        different from Previous stop this is implicit.
    :ivar change_of_service_requirements: Whether Service Requirements
        Change at this point.
    :ivar notice_assignments: NOTICEs for POINT IN JOURNEY PATTERN.
    :ivar request_stop: Whether stop is a request stop for this journey.
        Default is false.
    :ivar request_method: Method to Request Stop in this particular
        service pattern; if none specified, as as per stop.  +V1.1
    :ivar stop_use: Nature of use of stop, e.g. access, interchange
        only, or pass through. Default is Access.
    :ivar booking_arrangements: Booking Arrangements for stop if
        different from those for SERVICE JOURNEY.
    :ivar print: Whether the stop is included in printed media. Default
        is true. +v1.1
    :ivar dynamic: When STOP POINT IN JOURNEY PATTERN is to be
        publicised in dynamic media. Default is always. +v1.1
    """
    class Meta:
        name = "StopPointInJourneyPattern_VersionedChildStructure"

    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    onward_timing_link_ref: Optional[TimingLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_wait_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_time_or_wait_times: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "waitTimes",
                    "type": JourneyPatternWaitTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_service_link_ref: Optional[ServiceLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_alighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_boarding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_point_properties: Optional[FlexiblePointProperties] = field(
        default=None,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_destination_display: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfDestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_service_requirements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfServiceRequirements",
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
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_method: Optional[RequestMethodTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RequestMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_use: Optional[StopUseEnumeration] = field(
        default=None,
        metadata={
            "name": "StopUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
