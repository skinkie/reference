from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .luggage_spot_type_enumeration import LuggageSpotTypeEnumeration
from .spot_equipment_version_structure import SpotEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageSpotEquipmentVersionStructure(SpotEquipmentVersionStructure):
    class Meta:
        name = "LuggageSpotEquipment_VersionStructure"

    luggage_spot_type: Optional[LuggageSpotTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LuggageSpotType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headroom_for_luggage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeadroomForLuggage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_lockable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLockable",
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
