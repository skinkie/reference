from dataclasses import dataclass, field
from netex.fare_structure_element_price_versioned_child_structure import FareStructureElementPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementPrice(FareStructureElementPriceVersionedChildStructure):
    """A set of all possible price features of a FARE STRUCTURE ELEMENT: default total price, discount in value or percentage etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
