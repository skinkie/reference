from dataclasses import dataclass, field
from netex.usage_discount_right_version_structure import UsageDiscountRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageDiscountRight(UsageDiscountRightVersionStructure):
    """
    A FARE PRODUCT allowing a customer to benefit from discounts when consuming
    VALIDABLE ELEMENTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
