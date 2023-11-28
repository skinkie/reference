from dataclasses import dataclass, field
from netex.capped_discount_right_version_structure import CappedDiscountRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CappedDiscountRight(CappedDiscountRightVersionStructure):
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
