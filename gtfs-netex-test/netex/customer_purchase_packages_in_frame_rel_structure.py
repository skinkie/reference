from dataclasses import dataclass, field
from typing import List

from .fare_contract_entries_rel_structure import CustomerPurchasePackage
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerPurchasePackagesInFrame_RelStructure"

    customer_purchase_package: List[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
