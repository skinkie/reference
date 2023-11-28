from dataclasses import dataclass, field
from typing import Optional
from netex.access_feature_enumeration import AccessFeatureEnumeration
from netex.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.activated_equipment_ref import ActivatedEquipmentRef
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.assistance_service_ref import AssistanceServiceRef
from netex.battery_equipment_ref import BatteryEquipmentRef
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.catering_service_ref import CateringServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.check_constraint_delays_rel_structure import CheckConstraintDelaysRelStructure
from netex.check_constraint_throughputs_rel_structure import CheckConstraintThroughputsRelStructure
from netex.check_direction_enumeration import CheckDirectionEnumeration
from netex.check_process_type_enumeration import CheckProcessTypeEnumeration
from netex.check_service_enumeration import CheckServiceEnumeration
from netex.class_of_use_ref import ClassOfUseRef
from netex.communication_service_ref import CommunicationServiceRef
from netex.complaints_service_ref import ComplaintsServiceRef
from netex.congestion_enumeration import CongestionEnumeration
from netex.crossing_equipment_ref import CrossingEquipmentRef
from netex.customer_service_ref import CustomerServiceRef
from netex.cycle_storage_equipment_ref import CycleStorageEquipmentRef
from netex.entrance_equipment_ref import EntranceEquipmentRef
from netex.equipment_ref import EquipmentRef
from netex.escalator_equipment_ref import EscalatorEquipmentRef
from netex.facility_ref import FacilityRef
from netex.general_sign_ref import GeneralSignRef
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
from netex.passenger_equipment_ref import PassengerEquipmentRef
from netex.passenger_information_equipment_ref import PassengerInformationEquipmentRef
from netex.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.place_lighting_equipment_ref import PlaceLightingEquipmentRef
from netex.place_ref import PlaceRef
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
from netex.shelter_equipment_ref import ShelterEquipmentRef
from netex.sign_equipment_ref import SignEquipmentRef
from netex.site_equipment_ref import SiteEquipmentRef
from netex.staircase_equipment_ref import StaircaseEquipmentRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from netex.ticketing_equipment_ref import TicketingEquipmentRef
from netex.ticketing_service_ref import TicketingServiceRef
from netex.travelator_equipment_ref import TravelatorEquipmentRef
from netex.trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from netex.type_of_congestion_ref import TypeOfCongestionRef
from netex.type_of_equipment_ref import TypeOfEquipmentRef
from netex.vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from netex.vehicle_equipment_ref import VehicleEquipmentRef
from netex.vehicle_release_equipment_ref import VehicleReleaseEquipmentRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef
from netex.waiting_equipment_ref import WaitingEquipmentRef
from netex.waiting_room_equipment_ref import WaitingRoomEquipmentRef
from netex.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintVersionStructure(AssignmentVersionStructure1):
    """
    Type for a CHECK CONSTRAINT.

    :ivar place_ref:
    :ivar check_direction: For CHECK CONSTRAINTs associated with PATH
        LINKs, the direction in which the check applies. Forwards =
        from/to, backwards = to/from. For Check constraints associated
        with an external ENTRANCE, forwards is into the SITE, backwards
        is out of the SITE.
    :ivar check_process: Type of process that may occur at CHECK
        CONSTRAINT.
    :ivar check_service: Nature of service that may occur at CHECK
        CONSTRAINT.
    :ivar access_feature_type: Type of physical feature that may slow
        use of CHECK CONSTRAINT.
    :ivar congestion: Type of crowding that may slow use of CHECK
        CONSTRAINT.
    :ivar type_of_congestion_ref:
    :ivar class_of_use_ref:
    :ivar type_of_equipment_ref:
    :ivar facility_ref:
    :ivar choice:
    :ivar delays: Delays for CHECK CONSTRAINT .process.
    :ivar throughput: Throughput for CHECK CONSTRAINT.
    """
    class Meta:
        name = "CheckConstraint_VersionStructure"

    place_ref: Optional[PlaceRef] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_direction: Optional[CheckDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_process: Optional[CheckProcessTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckProcess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_service: Optional[CheckServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_feature_type: Optional[AccessFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    congestion: Optional[CongestionEnumeration] = field(
        default=None,
        metadata={
            "name": "Congestion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_congestion_ref: Optional[TypeOfCongestionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCongestionRef",
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
    type_of_equipment_ref: Optional[TypeOfEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facility_ref: Optional[FacilityRef] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
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
    delays: Optional[CheckConstraintDelaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    throughput: Optional[CheckConstraintThroughputsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
