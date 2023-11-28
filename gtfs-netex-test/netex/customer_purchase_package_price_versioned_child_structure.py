from dataclasses import dataclass, field
from typing import Optional
from netex.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackagePriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a CUSTOMER PURCHASE PACKAGE PRICEs.
    """
    class Meta:
        name = "CustomerPurchasePackagePrice_VersionedChildStructure"

    customer_purchase_package_ref_or_customer_purchase_package_element_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
