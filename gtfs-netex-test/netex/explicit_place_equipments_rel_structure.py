from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.crossing_equipment import CrossingEquipment
from netex.entrance_equipment import EntranceEquipment
from netex.escalator_equipment import EscalatorEquipment
from netex.general_sign_structure import GeneralSignStructure
from netex.heading_sign_structure import HeadingSignStructure
from netex.help_point_equipment import HelpPointEquipment
from netex.lift_equipment import LiftEquipment
from netex.other_place_equipment import OtherPlaceEquipment
from netex.passenger_safety_equipment import PassengerSafetyEquipment
from netex.place_lighting import PlaceLighting
from netex.place_sign_structure import PlaceSignStructure
from netex.queueing_equipment import QueueingEquipment
from netex.ramp_equipment import RampEquipment
from netex.rough_surface import RoughSurface
from netex.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.sanitary_equipment import SanitaryEquipment
from netex.staircase_equipment import StaircaseEquipment
from netex.ticket_validator_equipment import TicketValidatorEquipment
from netex.ticketing_equipment import TicketingEquipment
from netex.travelator_equipment import TravelatorEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExplicitPlaceEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    Items of fixed EQUIPMENT that may be located in places within the STOP PLACE.
    """
    class Meta:
        name = "explicitPlaceEquipments_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OtherPlaceEquipment",
                    "type": OtherPlaceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSignStructure,
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
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
