from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from netex.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.activated_equipment_ref import ActivatedEquipmentRef
from netex.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.assistance_service_ref import AssistanceServiceRef
from netex.authority_ref import AuthorityRef
from netex.battery_equipment_ref import BatteryEquipmentRef
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.catering_service_ref import CateringServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.class_of_use_ref import ClassOfUseRef
from netex.communication_service_ref import CommunicationServiceRef
from netex.companion_profile_ref import CompanionProfileRef
from netex.complaints_service_ref import ComplaintsServiceRef
from netex.crossing_equipment_ref import CrossingEquipmentRef
from netex.customer_service_ref import CustomerServiceRef
from netex.cycle_storage_equipment_ref import CycleStorageEquipmentRef
from netex.entrance_equipment_ref import EntranceEquipmentRef
from netex.equipment_ref import EquipmentRef
from netex.escalator_equipment_ref import EscalatorEquipmentRef
from netex.fare_class_enumeration import FareClassEnumeration
from netex.general_sign_ref import GeneralSignRef
from netex.group_of_operators_ref import GroupOfOperatorsRef
from netex.group_ticket_ref import GroupTicketRef
from netex.heading_sign_ref import HeadingSignRef
from netex.help_point_equipment_ref import HelpPointEquipmentRef
from netex.hire_service_ref import HireServiceRef
from netex.left_luggage_service_ref import LeftLuggageServiceRef
from netex.lift_equipment_ref import LiftEquipmentRef
from netex.local_service_ref import LocalServiceRef
from netex.lost_property_service_ref import LostPropertyServiceRef
from netex.luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from netex.luggage_service_ref import LuggageServiceRef
from netex.meeting_point_service_ref import MeetingPointServiceRef
from netex.money_service_ref import MoneyServiceRef
from netex.online_service_ref import OnlineServiceRef
from netex.operator_ref import OperatorRef
from netex.passenger_equipment_ref import PassengerEquipmentRef
from netex.passenger_information_equipment_ref import PassengerInformationEquipmentRef
from netex.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.passenger_seat_ref import PassengerSeatRef
from netex.place_lighting_equipment_ref import PlaceLightingEquipmentRef
from netex.place_sign_ref import PlaceSignRef
from netex.queueing_equipment_ref import QueueingEquipmentRef
from netex.ramp_equipment_ref import RampEquipmentRef
from netex.refuelling_equipment_ref import RefuellingEquipmentRef
from netex.retail_device_ref import RetailDeviceRef
from netex.retail_service_ref import RetailServiceRef
from netex.rough_surface_ref import RoughSurfaceRef
from netex.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.seating_equipment_ref import SeatingEquipmentRef
from netex.series_constraint_refs_rel_structure import SeriesConstraintRefsRelStructure
from netex.service_facility_set import ServiceFacilitySet
from netex.shelter_equipment_ref import ShelterEquipmentRef
from netex.sign_equipment_ref import SignEquipmentRef
from netex.site_equipment_ref import SiteEquipmentRef
from netex.staircase_equipment_ref import StaircaseEquipmentRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from netex.ticketing_equipment_ref import TicketingEquipmentRef
from netex.ticketing_service_ref import TicketingServiceRef
from netex.train_component_label_assignment_ref import TrainComponentLabelAssignmentRef
from netex.train_element_ref import TrainElementRef
from netex.travel_specification_journey_refs_rel_structure import TravelSpecificationJourneyRefsRelStructure
from netex.travel_specification_summary_endpoint_structure import TravelSpecificationSummaryEndpointStructure
from netex.travelator_equipment_ref import TravelatorEquipmentRef
from netex.trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from netex.type_of_fare_product_ref import TypeOfFareProductRef
from netex.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.user_profile_ref import UserProfileRef
from netex.vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from netex.vehicle_equipment_ref import VehicleEquipmentRef
from netex.vehicle_pooler_profile_ref import VehiclePoolerProfileRef
from netex.vehicle_release_equipment_ref import VehicleReleaseEquipmentRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef
from netex.waiting_equipment_ref import WaitingEquipmentRef
from netex.waiting_room_equipment_ref import WaitingRoomEquipmentRef
from netex.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelSpecificationSummaryViewStructure:
    """Summary of key aspects of TRAVEL SPECIFICATION.

    +V1.1. This data should all be derivable from the detailed
    specification. v+1.1

    :ivar origin: Origin of Travel.  Note that for a point-to-point
        TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT.
    :ivar destination: Destination of Travel. Note that for a point-to-
        point TARIFF the origin is assigned with a DISTANCE MATRIX
        ELEMENT.
    :ivar start: Start timw for trip or pass.
    :ivar end: End time for trip or pass.
    :ivar duration: DUration for trip or pass
    :ivar journeys: Specified journeys for trip.
    :ivar series_constraints: Routig for trip
    :ivar authority_ref_or_operator_ref_or_group_of_operators_ref:
    :ivar type_of_product_category_ref:
    :ivar type_of_fare_product_ref:
    :ivar fare_class:
    :ivar class_of_use_ref:
    :ivar
        vehicle_pooler_profile_ref_or_companion_profile_ref_or_user_profile_ref:
    :ivar group_ticket_ref:
    :ivar maximum_number_of_users: Maimum number of users on a GROUP
        TICKET.
    :ivar train_element_ref:
    :ivar train_component_label_assignment_ref:
    :ivar passenger_seat_ref:
    :ivar service_facility_set:
    :ivar choice:
    """
    origin: Optional[TravelSpecificationSummaryEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination: Optional[TravelSpecificationSummaryEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional[TravelSpecificationJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraints: Optional[SeriesConstraintRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref_or_operator_ref_or_group_of_operators_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_pooler_profile_ref_or_companion_profile_ref_or_user_profile_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    group_ticket_ref: Optional[GroupTicketRef] = field(
        default=None,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_users: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfUsers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_label_assignment_ref: Optional[TrainComponentLabelAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_seat_ref: Optional[PassengerSeatRef] = field(
        default=None,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set: Optional[ServiceFacilitySet] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySet",
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
                    "name": "RetailDeviceRef",
                    "type": RetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivatedEquipmentRef",
                    "type": ActivatedEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BatteryEquipmentRef",
                    "type": BatteryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefuellingEquipmentRef",
                    "type": RefuellingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipmentRef",
                    "type": VehicleChargingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringServiceRef",
                    "type": CateringServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailServiceRef",
                    "type": RetailServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyServiceRef",
                    "type": MoneyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireServiceRef",
                    "type": HireServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationServiceRef",
                    "type": CommunicationServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointServiceRef",
                    "type": MeetingPointServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageServiceRef",
                    "type": LeftLuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageServiceRef",
                    "type": LuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyServiceRef",
                    "type": LostPropertyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsServiceRef",
                    "type": ComplaintsServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerServiceRef",
                    "type": CustomerServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceServiceRef",
                    "type": AssistanceServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceRef",
                    "type": TicketingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleReleaseEquipmentRef",
                    "type": VehicleReleaseEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipmentRef",
                    "type": TicketValidatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipmentRef",
                    "type": TicketingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipmentRef",
                    "type": PassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipmentRef",
                    "type": CycleStorageEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipmentRef",
                    "type": TrolleyStandEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipmentRef",
                    "type": SeatingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipmentRef",
                    "type": ShelterEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageLockerEquipmentRef",
                    "type": LuggageLockerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipmentRef",
                    "type": WaitingRoomEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingEquipmentRef",
                    "type": WaitingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteEquipmentRef",
                    "type": SiteEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLightingEquipmentRef",
                    "type": PlaceLightingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurfaceRef",
                    "type": RoughSurfaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipmentRef",
                    "type": StaircaseEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipmentRef",
                    "type": QueueingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipmentRef",
                    "type": TravelatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipmentRef",
                    "type": EscalatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipmentRef",
                    "type": LiftEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipmentRef",
                    "type": CrossingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipmentRef",
                    "type": RampEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipmentRef",
                    "type": EntranceEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSignRef",
                    "type": HeadingSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSignRef",
                    "type": GeneralSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSignRef",
                    "type": PlaceSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipmentRef",
                    "type": SignEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipmentRef",
                    "type": RubbishDisposalEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipmentRef",
                    "type": HelpPointEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipmentRef",
                    "type": PassengerSafetyEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipmentRef",
                    "type": SanitaryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleRef",
                    "type": WheelchairVehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipmentRef",
                    "type": AccessVehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentRef",
                    "type": VehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEquipmentRef",
                    "type": PassengerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentRef",
                    "type": EquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
