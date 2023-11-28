from dataclasses import dataclass, field
from typing import List
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a CUSTOMER PURCHASE PACKAGE.
    """
    class Meta:
        name = "customerPurchasePackageRefs_RelStructure"

    customer_purchase_package_ref: List[CustomerPurchasePackageRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
