from dataclasses import dataclass

from .sale_discount_right_ref_structure import SaleDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRightRefStructure(SaleDiscountRightRefStructure):
    pass
