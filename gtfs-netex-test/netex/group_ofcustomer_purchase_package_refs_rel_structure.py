from dataclasses import dataclass, field

from .group_of_customer_purchase_packages_ref import GroupOfCustomerPurchasePackagesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfcustomerPurchasePackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupOfcustomerPurchasePackageRefs_RelStructure"

    group_of_customer_purchase_packages_ref: list[GroupOfCustomerPurchasePackagesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfCustomerPurchasePackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
