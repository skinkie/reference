from dataclasses import dataclass, field
from typing import Optional
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.time_unit_ref import TimeUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeUnitPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a TIME UNIT PRICEs.
    """
    class Meta:
        name = "TimeUnitPrice_VersionedChildStructure"

    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
