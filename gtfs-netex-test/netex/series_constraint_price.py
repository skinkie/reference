from dataclasses import dataclass
from .series_constraint_price_versioned_child_structure import (
    SeriesConstraintPriceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintPrice(SeriesConstraintPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
