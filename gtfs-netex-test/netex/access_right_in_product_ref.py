from dataclasses import dataclass
from netex.access_right_in_product_ref_structure import AccessRightInProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightInProductRef(AccessRightInProductRefStructure):
    """
    Reference to an ACCESS RIGHT IN PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
