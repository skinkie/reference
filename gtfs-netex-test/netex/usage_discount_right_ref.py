from dataclasses import dataclass
from netex.usage_discount_right_ref_structure import UsageDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageDiscountRightRef(UsageDiscountRightRefStructure):
    """
    Reference to a USAGE DISCOUNT RIGHT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
