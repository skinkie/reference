from dataclasses import dataclass, field
from netex.geographical_unit_prices_rel_structure import GeographicalUnitPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitPrice(GeographicalUnitPriceVersionedChildStructure):
    """A set of all possible price features of a GEOGRAPHICAL UNIT: default total price etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
