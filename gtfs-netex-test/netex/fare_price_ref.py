from dataclasses import dataclass
from netex.fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePriceRef(FarePriceRefStructure):
    """
    Reference to a FARE PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
