from dataclasses import dataclass
from netex.sale_discount_right_ref_structure import SaleDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SaleDiscountRightRef(SaleDiscountRightRefStructure):
    """
    Reference to a SALES DISCOUNT RIGHT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
