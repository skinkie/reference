from dataclasses import dataclass
from netex.capped_discount_right_ref_structure import CappedDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CappedDiscountRightRef(CappedDiscountRightRefStructure):
    """
    Reference to a CAPPED DISCOUNT RIGHT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
