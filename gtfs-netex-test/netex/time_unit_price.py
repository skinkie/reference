from dataclasses import dataclass, field
from netex.time_unit_price_versioned_child_structure import TimeUnitPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeUnitPrice(TimeUnitPriceVersionedChildStructure):
    """A set of all possible price features of a TIME UNIT: default total price etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
