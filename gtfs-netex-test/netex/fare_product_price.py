from dataclasses import dataclass
from .fare_product_price_versioned_child_structure import (
    FareProductPriceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductPrice(FareProductPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
