from dataclasses import dataclass

from .amount_of_price_unit_product_ref_structure import AmountOfPriceUnitProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AmountOfPriceUnitProductRef(AmountOfPriceUnitProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
