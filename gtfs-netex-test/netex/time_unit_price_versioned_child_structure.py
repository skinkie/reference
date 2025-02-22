from dataclasses import dataclass, field
from typing import Optional

from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .time_unit_ref import TimeUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeUnitPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "TimeUnitPrice_VersionedChildStructure"

    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
