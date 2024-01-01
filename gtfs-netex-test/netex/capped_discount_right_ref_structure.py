from dataclasses import dataclass
from .sale_discount_right_ref_structure import SaleDiscountRightRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRightRefStructure(SaleDiscountRightRefStructure):
    value: RestrictedVar
