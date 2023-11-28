from dataclasses import dataclass, field
from netex.time_interval_price_versioned_child_structure import TimeIntervalPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeIntervalPrice(TimeIntervalPriceVersionedChildStructure):
    """A set of all possible price features of a TIME INTERVAL: default total price etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
