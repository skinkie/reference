from dataclasses import dataclass, field
from typing import Union

from .access_vehicle_equipment import AccessVehicleEquipment
from .actual_vehicle_equipment import ActualVehicleEquipment
from .assistance_booking_service import AssistanceBookingService
from .assistance_service import AssistanceService
from .battery_equipment import BatteryEquipment
from .bed_equipment import BedEquipment
from .car_pooling_service import CarPoolingService
from .catering_service import CateringService
from .chauffeured_vehicle_service import ChauffeuredVehicleService
from .communication_service import CommunicationService
from .complaints_service import ComplaintsService
from .containment_aggregation_structure import ContainmentAggregationStructure
from .crossing_equipment import CrossingEquipment
from .customer_service import CustomerService
from .cycle_storage_equipment import CycleStorageEquipment
from .entrance_equipment import EntranceEquipment
from .entrance_sensor import EntranceSensor
from .escalator_equipment import EscalatorEquipment
from .general_sign import GeneralSign
from .heading_sign import HeadingSign
from .help_point_equipment import HelpPointEquipment
from .hire_service import HireService
from .left_luggage_service import LeftLuggageService
from .lift_call_equipment import LiftCallEquipment
from .lift_equipment import LiftEquipment
from .lost_property_service import LostPropertyService
from .luggage_service import LuggageService
from .luggage_spot_equipment import LuggageSpotEquipment
from .meeting_point_service import MeetingPointService
from .money_service import MoneyService
from .online_service import OnlineService
from .passenger_beacon_equipment import PassengerBeaconEquipment
from .passenger_information_equipment import PassengerInformationEquipment
from .passenger_safety_equipment import PassengerSafetyEquipment
from .place_lighting import PlaceLighting
from .place_sign import PlaceSign
from .queueing_equipment import QueueingEquipment
from .ramp_equipment import RampEquipment
from .refuelling_equipment import RefuellingEquipment
from .retail_device import RetailDevice
from .retail_service import RetailService
from .rough_surface import RoughSurface
from .rubbish_disposal_equipment import RubbishDisposalEquipment
from .sanitary_equipment import SanitaryEquipment
from .seat_equipment import SeatEquipment
from .seating_equipment import SeatingEquipment
from .sensor_equipment import SensorEquipment
from .shelter_equipment import ShelterEquipment
from .sign_equipment import SignEquipment
from .spot_equipment_1 import SpotEquipment1
from .spot_equipment_2 import SpotEquipment2
from .spot_sensor import SpotSensor
from .staircase_equipment import StaircaseEquipment
from .taxi_service import TaxiService
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticketing_equipment import TicketingEquipment
from .ticketing_service import TicketingService
from .travelator_equipment import TravelatorEquipment
from .trolley_stand_equipment import TrolleyStandEquipment
from .vehicle_charging_equipment import VehicleChargingEquipment
from .vehicle_release_equipment import VehicleReleaseEquipment
from .vehicle_rental_service import VehicleRentalService
from .vehicle_sharing_service import VehicleSharingService
from .waiting_room_equipment import WaitingRoomEquipment
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EquipmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "equipmentsInFrame_RelStructure"

    choice: list[
        Union[
            OnlineService,
            VehicleRentalService,
            VehicleSharingService,
            ChauffeuredVehicleService,
            CarPoolingService,
            TaxiService,
            AssistanceBookingService,
            CateringService,
            RetailService,
            MoneyService,
            HireService,
            CommunicationService,
            MeetingPointService,
            LostPropertyService,
            LeftLuggageService,
            ComplaintsService,
            CustomerService,
            LuggageService,
            AssistanceService,
            TicketingService,
            RetailDevice,
            BatteryEquipment,
            EntranceSensor,
            SpotSensor,
            SensorEquipment,
            LuggageSpotEquipment,
            BedEquipment,
            SeatEquipment,
            SpotEquipment1,
            SpotEquipment2,
            VehicleReleaseEquipment,
            RefuellingEquipment,
            VehicleChargingEquipment,
            CycleStorageEquipment,
            SeatingEquipment,
            ShelterEquipment,
            TrolleyStandEquipment,
            WaitingRoomEquipment,
            CrossingEquipment,
            QueueingEquipment,
            EntranceEquipment,
            RampEquipment,
            LiftCallEquipment,
            LiftEquipment,
            TravelatorEquipment,
            StaircaseEquipment,
            EscalatorEquipment,
            PlaceLighting,
            RoughSurface,
            GeneralSign,
            HeadingSign,
            PlaceSign,
            SignEquipment,
            PassengerInformationEquipment,
            RubbishDisposalEquipment,
            PassengerBeaconEquipment,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            SanitaryEquipment,
            TicketValidatorEquipment,
            TicketingEquipment,
            WheelchairVehicleEquipment,
            AccessVehicleEquipment,
            ActualVehicleEquipment,
        ]
    ] = field(
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
                    "name": "EntranceSensor",
                    "type": EntranceSensor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpotSensor",
                    "type": SpotSensor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SensorEquipment",
                    "type": SensorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageSpotEquipment",
                    "type": LuggageSpotEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BedEquipment",
                    "type": BedEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatEquipment",
                    "type": SeatEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpotEquipment",
                    "type": SpotEquipment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpotEquipment_",
                    "type": SpotEquipment2,
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
                    "name": "LiftCallEquipment",
                    "type": LiftCallEquipment,
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
                    "name": "PassengerBeaconEquipment",
                    "type": PassengerBeaconEquipment,
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
                {
                    "name": "ActualVehicleEquipment",
                    "type": ActualVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
