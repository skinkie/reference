from dataclasses import dataclass, field
from typing import Optional
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a FARE STRUCTURE ELEMENT PRICEs.
    """
    class Meta:
        name = "FareStructureElementPrice_VersionedChildStructure"

    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
