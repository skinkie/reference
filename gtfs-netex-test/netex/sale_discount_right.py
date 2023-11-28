from dataclasses import dataclass, field
from netex.sale_discount_right_version_structure import SaleDiscountRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SaleDiscountRight(SaleDiscountRightVersionStructure):
    """
    A FARE PRODUCT allowing a customer to benefit from discounts when purchasing
    SALES OFFER PACKAGEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
