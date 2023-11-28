from dataclasses import dataclass, field
from typing import List
from netex.access_vehicle_equipment import AccessVehicleEquipment
from netex.assistance_booking_service import AssistanceBookingService
from netex.assistance_service import AssistanceService
from netex.battery_equipment import BatteryEquipment
from netex.car_pooling_service import CarPoolingService
from netex.catering_service import CateringService
from netex.chauffeured_vehicle_service import ChauffeuredVehicleService
from netex.communication_service import CommunicationService
from netex.complaints_service import ComplaintsService
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.crossing_equipment import CrossingEquipment
from netex.customer_service import CustomerService
from netex.cycle_storage_equipment import CycleStorageEquipment
from netex.entrance_equipment import EntranceEquipment
from netex.escalator_equipment import EscalatorEquipment
from netex.general_sign import GeneralSign
from netex.heading_sign import HeadingSign
from netex.help_point_equipment import HelpPointEquipment
from netex.hire_service import HireService
from netex.left_luggage_service import LeftLuggageService
from netex.lift_equipment import LiftEquipment
from netex.lost_property_service import LostPropertyService
from netex.luggage_service import LuggageService
from netex.meeting_point_service import MeetingPointService
from netex.money_service import MoneyService
from netex.online_service import OnlineService
from netex.passenger_information_equipment import PassengerInformationEquipment
from netex.passenger_safety_equipment import PassengerSafetyEquipment
from netex.place_lighting import PlaceLighting
from netex.place_sign import PlaceSign
from netex.queueing_equipment import QueueingEquipment
from netex.ramp_equipment import RampEquipment
from netex.refuelling_equipment import RefuellingEquipment
from netex.retail_device import RetailDevice
from netex.retail_service import RetailService
from netex.rough_surface import RoughSurface
from netex.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.sanitary_equipment import SanitaryEquipment
from netex.seating_equipment import SeatingEquipment
from netex.shelter_equipment import ShelterEquipment
from netex.sign_equipment import SignEquipment
from netex.staircase_equipment import StaircaseEquipment
from netex.taxi_service import TaxiService
from netex.ticket_validator_equipment import TicketValidatorEquipment
from netex.ticketing_equipment import TicketingEquipment
from netex.ticketing_service import TicketingService
from netex.travelator_equipment import TravelatorEquipment
from netex.trolley_stand_equipment import TrolleyStandEquipment
from netex.vehicle_charging_equipment import VehicleChargingEquipment
from netex.vehicle_release_equipment import VehicleReleaseEquipment
from netex.vehicle_rental_service import VehicleRentalService
from netex.vehicle_sharing_service import VehicleSharingService
from netex.waiting_room_equipment import WaitingRoomEquipment
from netex.wheelchair_vehicle_equipment import WheelchairVehicleEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of EQUIPMENT.
    """
    class Meta:
        name = "equipmentsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineService",
                    "type": OnlineService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalService",
                    "type": VehicleRentalService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingService",
                    "type": VehicleSharingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleService",
                    "type": ChauffeuredVehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingService",
                    "type": CarPoolingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiService",
                    "type": TaxiService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringService",
                    "type": CateringService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailService",
                    "type": RetailService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyService",
                    "type": MoneyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireService",
                    "type": HireService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationService",
                    "type": CommunicationService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointService",
                    "type": MeetingPointService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyService",
                    "type": LostPropertyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageService",
                    "type": LeftLuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsService",
                    "type": ComplaintsService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerService",
                    "type": CustomerService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageService",
                    "type": LuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceService",
                    "type": AssistanceService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingService",
                    "type": TicketingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDevice",
                    "type": RetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BatteryEquipment",
                    "type": BatteryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleReleaseEquipment",
                    "type": VehicleReleaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefuellingEquipment",
                    "type": RefuellingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipment",
                    "type": VehicleChargingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipment",
                    "type": CycleStorageEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipment",
                    "type": SeatingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipment",
                    "type": ShelterEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipment",
                    "type": TrolleyStandEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipment",
                    "type": WaitingRoomEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipment",
                    "type": SignEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipment",
                    "type": PassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleEquipment",
                    "type": WheelchairVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipment",
                    "type": AccessVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
