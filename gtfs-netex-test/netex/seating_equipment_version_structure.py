from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .waiting_equipment_version_structure import (
    WaitingEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatingEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    class Meta:
        name = "SeatingEquipment_VersionStructure"

    armrest: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Armrest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    seat_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeatHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
