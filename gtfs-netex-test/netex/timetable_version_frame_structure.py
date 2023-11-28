from dataclasses import dataclass, field
from typing import List, Optional
from netex.accessibility_assessment import AccessibilityAssessment
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.compound_train_ref import CompoundTrainRef
from netex.contained_availability_conditions_rel_structure import ContainedAvailabilityConditionsRelStructure
from netex.coupled_journeys_in_frame_rel_structure import CoupledJourneysInFrameRelStructure
from netex.default_interchangse_in_frame_rel_structure import DefaultInterchangseInFrameRelStructure
from netex.flexible_service_properties_in_frame_rel_structure import FlexibleServicePropertiesInFrameRelStructure
from netex.frequency_groups_in_frame_rel_structure import FrequencyGroupsInFrameRelStructure
from netex.group_of_links_in_frame_rel_structure import GroupOfLinksInFrameRelStructure
from netex.groups_of_services_in_frame_rel_structure import GroupsOfServicesInFrameRelStructure
from netex.interchange_rules_in_frame_rel_structure import InterchangeRulesInFrameRelStructure
from netex.journey_accounting_ref import JourneyAccountingRef
from netex.journey_accountings_in_frame_rel_structure import JourneyAccountingsInFrameRelStructure
from netex.journey_interchanges_in_frame_rel_structure import JourneyInterchangesInFrameRelStructure
from netex.journey_meetings_in_frame_rel_structure import JourneyMeetingsInFrameRelStructure
from netex.journey_part_couples_in_frame_rel_structure import JourneyPartCouplesInFrameRelStructure
from netex.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.line_view import LineView
from netex.network_view import NetworkView
from netex.notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from netex.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.operator_view import OperatorView
from netex.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.time_demand_type_assignments_in_frame_rel_structure import TimeDemandTypeAssignmentsInFrameRelStructure
from netex.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.train_numbers_in_frame_rel_structure import TrainNumbersInFrameRelStructure
from netex.train_ref import TrainRef
from netex.transport_type_ref import TransportTypeRef
from netex.types_of_service_in_frame_rel_structure import TypesOfServiceInFrameRelStructure
from netex.vehicle_journey_stop_assignments_in_frame_rel_structure_2 import VehicleJourneyStopAssignmentsInFrameRelStructure2
from netex.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.vehicle_type_ref import VehicleTypeRef
from netex.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetableVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for TIMETABLE FRAME.

    :ivar vehicle_modes: Modes of VEHICLE JOURNEYs in timetable.
    :ivar headway_service: Whether this is a Headway SERVICE, that is,
        one shown as operating at a prescribed interval rather than to a
        fixed timetable.
    :ivar monitored: Whether VEHICLE JOURNEYs of line are normally
        monitored. Provides a default value for the Monitored element on
        individual journeys of the timetable.
    :ivar network_view:
    :ivar line_view:
    :ivar operator_view:
    :ivar service_calendar_frame_ref:
    :ivar default_mode: Default VEHICLE MODE to use on JOURNEYs in
        TIMETABLE.
    :ivar journey_accounting_ref:
    :ivar booking_times: When bookings can be made for a SERVICE.
    :ivar accessibility_assessment:
    :ivar choice:
    :ivar time_demand_types: TIME DEMAND TYPEs in frame.
    :ivar time_demand_type_assignments: TIME DEMAND TYPE ASSIGNMENTs in
        frame.
    :ivar timing_link_groups: TIMING LINK GROUPs in frame.
    :ivar vehicle_journeys: VEHICLE JOURNEYs in frame.
    :ivar frequency_groups: FREQUENCY GROUPs  In frame. Can be used to
        template VEHICLE JOURNEYs.
    :ivar groups_of_services: Groupings of Journeys In frame. Can be
        used to define inbound and outbound beds for a matrix
        presentation of the JORUNEYs in the TIMETABLE.
    :ivar train_numbers: TRAIN NUMBERs in frame.
    :ivar journey_part_couples: JOURNEY COUPLINGs  in frame.
    :ivar coupled_journeys: JOURNEY COUPLINGs  in frame.
    :ivar service_facility_sets: SERVICE FACILITies  in frame.
    :ivar types_of_service: TYPEs of SERVICE in frame.
    :ivar flexible_service_properties: FLEXIBLE SERVICE PROPERTIES in
        frame.
    :ivar vehicle_journey_stop_assignments: VEHICLE JOURNEY STOP
        ASSIGNMENTs in frame.
    :ivar notices: NOTICEs in frame.
    :ivar notice_assignments: NOTICE ASSIGNMENTs in frame.
    :ivar journey_meetings: JOURNEY MEETINGs in frame.
    :ivar journey_interchanges: INTERCHANGES in frame.
    :ivar default_interchanges: DEFAULT INTERCHANGES in frame.
    :ivar interchange_rules: INTERCHANGE RULEs in frame.
    :ivar vehicle_types: VEHICLE TYPEs in frame.
    :ivar journey_accountings: VEHICLE TYPEs in frame.
    """
    class Meta:
        name = "Timetable_VersionFrameStructure"

    vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_view: Optional[NetworkView] = field(
        default=None,
        metadata={
            "name": "NetworkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_view: Optional[LineView] = field(
        default=None,
        metadata={
            "name": "LineView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_view: Optional[OperatorView] = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame_ref: Optional[ServiceCalendarFrameRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "DefaultMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accounting_ref: Optional[JourneyAccountingRef] = field(
        default=None,
        metadata={
            "name": "JourneyAccountingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_times: Optional[ContainedAvailabilityConditionsRelStructure] = field(
        default=None,
        metadata={
            "name": "bookingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    time_demand_types: Optional[TimeDemandTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_assignments: Optional[TimeDemandTypeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_groups: Optional[GroupOfLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timingLinkGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journeys: Optional[JourneysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_groups: Optional[FrequencyGroupsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "frequencyGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_services: Optional[GroupsOfServicesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_numbers: Optional[TrainNumbersInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couples: Optional[JourneyPartCouplesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPartCouples",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    coupled_journeys: Optional[CoupledJourneysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "coupledJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_sets: Optional[ServiceFacilitySetsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "serviceFacilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_service: Optional[TypesOfServiceInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_properties: Optional[FlexibleServicePropertiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "flexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_stop_assignments: Optional[VehicleJourneyStopAssignmentsInFrameRelStructure2] = field(
        default=None,
        metadata={
            "name": "vehicleJourneyStopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notices: Optional[NoticesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_meetings: Optional[JourneyMeetingsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyMeetings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_interchanges: Optional[JourneyInterchangesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_interchanges: Optional[DefaultInterchangseInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "defaultInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rules: Optional[InterchangeRulesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "interchangeRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_types: Optional[VehicleTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accountings: Optional[JourneyAccountingsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyAccountings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
