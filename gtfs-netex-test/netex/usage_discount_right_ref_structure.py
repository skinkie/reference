from dataclasses import dataclass
from netex.fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageDiscountRightRefStructure(FareProductRefStructure):
    """
    Type for Reference to a USAGE DISCOUNT RIGHT.
    """
