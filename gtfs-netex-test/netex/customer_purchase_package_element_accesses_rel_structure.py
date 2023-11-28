from dataclasses import dataclass, field
from typing import List
from netex.customer_purchase_package_element_access import CustomerPurchasePackageElementAccess
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageElementAccessesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CUSTOMER PURCHASE PACKAGE ELEMENT ACCESS..
    """
    class Meta:
        name = "customerPurchasePackageElementAccesses_RelStructure"

    customer_purchase_package_element_access: List[CustomerPurchasePackageElementAccess] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElementAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
