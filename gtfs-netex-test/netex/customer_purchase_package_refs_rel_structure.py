from dataclasses import dataclass, field

from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerPurchasePackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerPurchasePackageRefs_RelStructure"

    customer_purchase_package_ref: list[CustomerPurchasePackageRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
