from dataclasses import dataclass

from .sale_discount_right_version_structure import SaleDiscountRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SaleDiscountRight(SaleDiscountRightVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
