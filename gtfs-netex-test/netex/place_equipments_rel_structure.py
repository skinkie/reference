from dataclasses import dataclass, field
from typing import List
from netex.access_vehicle_equipment import AccessVehicleEquipment
from netex.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.battery_equipment import BatteryEquipment
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.crossing_equipment import CrossingEquipment
from netex.crossing_equipment_ref import CrossingEquipmentRef
from netex.cycle_storage_equipment import CycleStorageEquipment
from netex.cycle_storage_equipment_ref import CycleStorageEquipmentRef
from netex.entrance_equipment import EntranceEquipment
from netex.entrance_equipment_ref import EntranceEquipmentRef
from netex.escalator_equipment import EscalatorEquipment
from netex.escalator_equipment_ref import EscalatorEquipmentRef
from netex.general_sign import GeneralSign
from netex.general_sign_ref import GeneralSignRef
from netex.heading_sign import HeadingSign
from netex.heading_sign_ref import HeadingSignRef
from netex.help_point_equipment import HelpPointEquipment
from netex.help_point_equipment_ref import HelpPointEquipmentRef
from netex.lift_equipment import LiftEquipment
from netex.lift_equipment_ref import LiftEquipmentRef
from netex.luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from netex.passenger_equipment_ref import PassengerEquipmentRef
from netex.passenger_information_equipment import PassengerInformationEquipment
from netex.passenger_information_equipment_ref import PassengerInformationEquipmentRef
from netex.passenger_safety_equipment import PassengerSafetyEquipment
from netex.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.place_lighting import PlaceLighting
from netex.place_lighting_equipment_ref import PlaceLightingEquipmentRef
from netex.place_sign import PlaceSign
from netex.place_sign_ref import PlaceSignRef
from netex.queueing_equipment import QueueingEquipment
from netex.queueing_equipment_ref import QueueingEquipmentRef
from netex.ramp_equipment import RampEquipment
from netex.ramp_equipment_ref import RampEquipmentRef
from netex.refuelling_equipment import RefuellingEquipment
from netex.retail_device import RetailDevice
from netex.rough_surface import RoughSurface
from netex.rough_surface_ref import RoughSurfaceRef
from netex.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.sanitary_equipment import SanitaryEquipment
from netex.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.seating_equipment import SeatingEquipment
from netex.seating_equipment_ref import SeatingEquipmentRef
from netex.shelter_equipment import ShelterEquipment
from netex.shelter_equipment_ref import ShelterEquipmentRef
from netex.sign_equipment import SignEquipment
from netex.sign_equipment_ref import SignEquipmentRef
from netex.site_equipment_ref import SiteEquipmentRef
from netex.staircase_equipment import StaircaseEquipment
from netex.staircase_equipment_ref import StaircaseEquipmentRef
from netex.ticket_validator_equipment import TicketValidatorEquipment
from netex.ticketing_equipment import TicketingEquipment
from netex.travelator_equipment import TravelatorEquipment
from netex.travelator_equipment_ref import TravelatorEquipmentRef
from netex.trolley_stand_equipment import TrolleyStandEquipment
from netex.trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from netex.vehicle_charging_equipment import VehicleChargingEquipment
from netex.vehicle_equipment_ref import VehicleEquipmentRef
from netex.vehicle_release_equipment import VehicleReleaseEquipment
from netex.waiting_equipment_ref import WaitingEquipmentRef
from netex.waiting_room_equipment import WaitingRoomEquipment
from netex.waiting_room_equipment_ref import WaitingRoomEquipmentRef
from netex.wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from netex.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LOCAL SERVICEs.
    """
    class Meta:
        name = "placeEquipments_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
