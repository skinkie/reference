from dataclasses import dataclass

from .capped_discount_right_ref_structure import CappedDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CappedDiscountRightRef(CappedDiscountRightRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
