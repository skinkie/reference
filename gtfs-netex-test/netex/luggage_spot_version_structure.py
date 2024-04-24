from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .locatable_spot_version_structure import LocatableSpotVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageSpotVersionStructure(LocatableSpotVersionStructure):
    class Meta:
        name = "LuggageSpot_VersionStructure"

    height_from_floor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
