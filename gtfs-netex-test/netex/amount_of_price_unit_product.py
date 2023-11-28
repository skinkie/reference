from dataclasses import dataclass, field
from netex.amount_of_price_unit_product_version_structure import AmountOfPriceUnitProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AmountOfPriceUnitProduct(AmountOfPriceUnitProductVersionStructure):
    """A FARE PRODUCT consisting in a stored value of PRICE UNITs: an amount of money on an electronic purse, amount of units on a value card etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
