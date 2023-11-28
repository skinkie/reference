from dataclasses import dataclass, field
from typing import List
from netex.group_of_customer_purchase_packages_ref import GroupOfCustomerPurchasePackagesRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfcustomerPurchasePackageRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a CUSTOMER PURCHASE PACKAGE.
    """
    class Meta:
        name = "groupOfcustomerPurchasePackageRefs_RelStructure"

    group_of_customer_purchase_packages_ref: List[GroupOfCustomerPurchasePackagesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfCustomerPurchasePackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
