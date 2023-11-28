from dataclasses import dataclass
from netex.preassigned_fare_product_ref_structure import PreassignedFareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SupplementProductRefStructure(PreassignedFareProductRefStructure):
    """
    Type for Reference to a SUPPLEMENT PRODUCT.
    """
