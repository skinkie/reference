from dataclasses import dataclass
from .sale_discount_right_version_structure import (
    SaleDiscountRightVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SaleDiscountRight(SaleDiscountRightVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
