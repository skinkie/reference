from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_purchase_package_element import CustomerPurchasePackageElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerPurchasePackageElements_RelStructure"

    customer_purchase_package_element: list[CustomerPurchasePackageElement] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
