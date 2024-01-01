from dataclasses import dataclass
from .amount_of_price_unit_product_version_structure import (
    AmountOfPriceUnitProductVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AmountOfPriceUnitProduct(AmountOfPriceUnitProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
