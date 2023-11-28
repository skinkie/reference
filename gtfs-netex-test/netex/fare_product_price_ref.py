from dataclasses import dataclass
from netex.fare_product_price_ref_structure import FareProductPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductPriceRef(FareProductPriceRefStructure):
    """
    Reference to a FARE PRODUCT PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
