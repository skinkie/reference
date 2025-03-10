from dataclasses import dataclass, field
from typing import Optional

from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FulfilmentMethodPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "FulfilmentMethodPrice_VersionedChildStructure"

    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
