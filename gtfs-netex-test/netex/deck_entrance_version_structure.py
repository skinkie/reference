from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .deck_component_version_structure import DeckComponentVersionStructure
from .deck_entrance_type_enumeration import DeckEntranceTypeEnumeration
from .sensors_in_entrance_rel_structure import SensorsInEntranceRelStructure
from .type_of_deck_entrance_ref import TypeOfDeckEntranceRef
from .vehicle_side_enumeration import VehicleSideEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceVersionStructure(DeckComponentVersionStructure):
    class Meta:
        name = "DeckEntrance_VersionStructure"

    vehicle_side: Optional[VehicleSideEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleSide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance_from_front: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DistanceFromFront",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sequence_from_front: Optional[int] = field(
        default=None,
        metadata={
            "name": "SequenceFromFront",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_ground: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromGround",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_entrance_type: Optional[DeckEntranceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeckEntranceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_deck_entrance_ref: Optional[TypeOfDeckEntranceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDeckEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_emergency_exit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsEmergencyExit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_automatic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAutomatic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sensors_in_entrance: Optional[SensorsInEntranceRelStructure] = field(
        default=None,
        metadata={
            "name": "sensorsInEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
