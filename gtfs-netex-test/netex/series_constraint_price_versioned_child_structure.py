from dataclasses import dataclass, field
from typing import Optional
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a SERIES CONSTRAINT PRICEs.
    """
    class Meta:
        name = "SeriesConstraintPrice_VersionedChildStructure"

    series_constraint_ref: Optional[SeriesConstraintRef] = field(
        default=None,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
