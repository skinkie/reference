from dataclasses import dataclass

from .fare_product_price_ref_structure import FareProductPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareProductPriceRef(FareProductPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
