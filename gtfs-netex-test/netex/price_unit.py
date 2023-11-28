from dataclasses import dataclass, field
from netex.price_unit_version_structure import PriceUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PriceUnit(PriceUnitVersionStructure):
    """A unit to express prices: amount of currency, abstract fare unit, ticket unit or token etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
