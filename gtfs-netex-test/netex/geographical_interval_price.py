from dataclasses import dataclass, field
from netex.geographical_interval_price_versioned_child_structure import GeographicalIntervalPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalPrice(GeographicalIntervalPriceVersionedChildStructure):
    """A set of all possible price features of a GEOGRAPHICAL INTERVAL: default total price etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
