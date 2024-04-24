from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .locatable_spot_version_structure import LocatableSpotVersionStructure
from .seat_context_enumeration import SeatContextEnumeration
from .table_type_enumeration import TableTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpotVersionStructure(LocatableSpotVersionStructure):
    class Meta:
        name = "PassengerSpot_VersionStructure"

    seat_context: Optional[SeatContextEnumeration] = field(
        default=None,
        metadata={
            "name": "SeatContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    table_type: Optional[TableTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TableType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_armrest: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasArmrest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    leg_space: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LegSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_tray: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasTray",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_power: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
