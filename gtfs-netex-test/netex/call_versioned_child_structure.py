from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.arrival_structure import ArrivalStructure
from netex.booking_arrangements_structure import BookingArrangementsStructure
from netex.departure_structure import DepartureStructure
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_view import DestinationDisplayView
from netex.dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.flexible_point_properties import FlexiblePointProperties
from netex.frequency_structure import FrequencyStructure
from netex.multilingual_string import MultilingualString
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.onward_service_link_view import OnwardServiceLinkView
from netex.onward_timing_link_view import OnwardTimingLinkView
from netex.passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from netex.passenger_carrying_requirements_view import PassengerCarryingRequirementsView
from netex.point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure
from netex.request_method_type_enumeration import RequestMethodTypeEnumeration
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.scheduled_stop_point_view import ScheduledStopPointView
from netex.service_journey_ref import ServiceJourneyRef
from netex.service_link_ref_structure import ServiceLinkRefStructure
from netex.stop_use_enumeration import StopUseEnumeration
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.train_size import TrainSize
from netex.vehicle_equipments_rel_structure import VehicleEquipmentsRelStructure
from netex.vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CallVersionedChildStructure(VersionedChildStructure):
    """
    Data type for CALL.

    :ivar visit_number: Count of number of visits to this stop - as per
        SIRI use. Default is 1
    :ivar
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view:
    :ivar onward_timing_link_view:
    :ivar onward_service_link_ref_or_onward_service_link_view:
    :ivar timing_point_status: Nature of TIMING POINT. Default is
        primary.
    :ivar template_service_journey_ref_or_service_journey_ref:
    :ivar point_in_journey_pattern_ref: Point in JOURNEY PATTERN upon
        which this call is based. Can be used to obtain full association
        sets.
    :ivar arrival: Arrival at CALL.
    :ivar departure: Departure from a CALL.
    :ivar frequency: Frequency of service at CALL.
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
    :ivar
        passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view:
    :ivar train_size:
    :ivar equipments: VEHICLE EQUIPMENT available on service.
    :ivar note: Text annotation that applies to this CALL. This is for
        internal use. Customer facing should be added to footnote.
    :ivar order: Order of Call within Journey.
    :ivar constrained:
    """
    class Meta:
        name = "Call_VersionedChildStructure"

    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view: Optional[object] = field(
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
                {
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    onward_timing_link_view: Optional[OnwardTimingLinkView] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_service_link_ref_or_onward_service_link_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnwardServiceLinkRef",
                    "type": ServiceLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardServiceLinkView",
                    "type": OnwardServiceLinkView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    timing_point_status: Optional[TimingPointStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey_ref_or_service_journey_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    point_in_journey_pattern_ref: Optional[PointInJourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "PointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival: Optional[ArrivalStructure] = field(
        default=None,
        metadata={
            "name": "Arrival",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure: Optional[DepartureStructure] = field(
        default=None,
        metadata={
            "name": "Departure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
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
    passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipments: Optional[VehicleEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Note",
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
    constrained: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
