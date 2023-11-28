from dataclasses import dataclass
from netex.supplement_product_ref_structure import SupplementProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SupplementProductRef(SupplementProductRefStructure):
    """
    Reference to a SUPPLEMENT PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
