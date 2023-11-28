from dataclasses import dataclass
from netex.type_of_fare_product_ref_structure import TypeOfFareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareProductRef(TypeOfFareProductRefStructure):
    """
    Reference to a TYPE OF FARE PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
