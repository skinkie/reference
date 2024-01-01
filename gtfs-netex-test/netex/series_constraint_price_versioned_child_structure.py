from dataclasses import dataclass, field
from typing import Optional
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .series_constraint_ref import SeriesConstraintRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "SeriesConstraintPrice_VersionedChildStructure"

    series_constraint_ref: Optional[SeriesConstraintRef] = field(
        default=None,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
