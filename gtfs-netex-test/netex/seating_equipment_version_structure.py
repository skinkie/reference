from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.waiting_equipment_version_structure import WaitingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeatingEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    """
    Type for a SEATING EQUIPMENT.

    :ivar armrest: Whether there is an armrest. +v1.1
    :ivar seat_height: Height of the seating +v1.1)
    """
    class Meta:
        name = "SeatingEquipment_VersionStructure"

    armrest: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Armrest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    seat_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeatHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
