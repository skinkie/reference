from dataclasses import dataclass, field
from typing import Optional
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a GEOGRAPHICAL INTERVAL PRICEs.
    """
    class Meta:
        name = "GeographicalIntervalPrice_VersionedChildStructure"

    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
