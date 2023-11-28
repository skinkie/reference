from dataclasses import dataclass
from netex.customer_purchase_package_element_ref_structure import CustomerPurchasePackageElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageElementRef(CustomerPurchasePackageElementRefStructure):
    """
    Reference to a CUSTOMER PURCHASE PACKAGE ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
