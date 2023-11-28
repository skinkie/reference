from dataclasses import dataclass, field
from netex.fare_product_price_versioned_child_structure import FareProductPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductPrice(FareProductPriceVersionedChildStructure):
    """
    A set of all possible price features of a FARE PRODUCT default total price,
    discount in value or percentage etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
