from dataclasses import dataclass, field
from typing import Optional
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a FULFILMENT METHOD PRICE.
    """
    class Meta:
        name = "FulfilmentMethodPrice_VersionedChildStructure"

    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
