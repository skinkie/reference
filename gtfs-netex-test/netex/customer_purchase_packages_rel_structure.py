from dataclasses import dataclass, field
from typing import List
from netex.customer_purchase_package import CustomerPurchasePackage
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackagesRelStructure(OneToManyRelationshipStructure):
    """
    Type for containment in frame of CUSTOMER PURCHASE PACKAGE.
    """
    class Meta:
        name = "customerPurchasePackages_RelStructure"

    customer_purchase_package_or_customer_purchase_package_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackage",
                    "type": CustomerPurchasePackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
