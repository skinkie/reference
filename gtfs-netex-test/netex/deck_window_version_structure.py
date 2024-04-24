from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .deck_component_version_structure import DeckComponentVersionStructure
from .deck_window_type_enumeration import DeckWindowTypeEnumeration
from .vehicle_side_enumeration import VehicleSideEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckWindowVersionStructure(DeckComponentVersionStructure):
    class Meta:
        name = "DeckWindow_VersionStructure"

    sequence_from_front: Optional[int] = field(
        default=None,
        metadata={
            "name": "SequenceFromFront",
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
    height_from_floor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_side: Optional[VehicleSideEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleSide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_window_type: Optional[DeckWindowTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeckWindowType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_blind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasBlind",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_be_opened: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeOpened",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
