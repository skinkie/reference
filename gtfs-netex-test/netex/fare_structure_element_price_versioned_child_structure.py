from dataclasses import dataclass, field
from typing import Optional

from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareStructureElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "FareStructureElementPrice_VersionedChildStructure"

    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
