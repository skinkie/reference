from dataclasses import dataclass

from .fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class UsageDiscountRightRefStructure(FareProductRefStructure):
    pass
