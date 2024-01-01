from dataclasses import dataclass
from .fare_product_ref_structure import FareProductRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SaleDiscountRightRefStructure(FareProductRefStructure):
    value: RestrictedVar
