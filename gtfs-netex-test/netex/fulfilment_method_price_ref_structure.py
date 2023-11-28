from dataclasses import dataclass
from netex.fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodPriceRefStructure(FarePriceRefStructure):
    """
    Type for Reference to a FULFILMENT METHOD PRICE.
    """
