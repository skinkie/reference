from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .spot_equipment_version_structure import SpotEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatEquipmentVersionStructure(SpotEquipmentVersionStructure):
    class Meta:
        name = "SeatEquipment_VersionStructure"

    seat_back_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeatBackHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    seat_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeatDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_foldup: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFoldup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_reclining: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsReclining",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
