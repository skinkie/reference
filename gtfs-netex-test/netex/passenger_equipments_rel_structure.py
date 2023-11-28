from dataclasses import dataclass, field
from typing import List
from netex.access_vehicle_equipment import AccessVehicleEquipment
from netex.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.help_point_equipment import HelpPointEquipment
from netex.help_point_equipment_ref import HelpPointEquipmentRef
from netex.passenger_equipment_ref import PassengerEquipmentRef
from netex.passenger_information_equipment import PassengerInformationEquipment
from netex.passenger_safety_equipment import PassengerSafetyEquipment
from netex.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.sanitary_equipment import SanitaryEquipment
from netex.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.ticket_validator_equipment import TicketValidatorEquipment
from netex.ticketing_equipment import TicketingEquipment
from netex.vehicle_equipment_ref import VehicleEquipmentRef
from netex.wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from netex.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LOCAL SERVICEs.
    """
    class Meta:
        name = "passengerEquipments_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
