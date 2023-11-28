from dataclasses import dataclass, field
from netex.customer_purchase_package_price_versioned_child_structure import CustomerPurchasePackagePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackagePrice(CustomerPurchasePackagePriceVersionedChildStructure):
    """A set of all possible price features of a CUSTOMER PURCHASE PACKAGE ELEMENT: default total price, discount in value or percentage etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
