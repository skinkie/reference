from dataclasses import dataclass

from .amount_of_price_unit_product_version_structure import AmountOfPriceUnitProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AmountOfPriceUnitProduct(AmountOfPriceUnitProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
