from dataclasses import dataclass
from netex.fulfilment_method_price_ref_structure import FulfilmentMethodPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodPriceRef(FulfilmentMethodPriceRefStructure):
    """
    Reference to a FULFILMENT METHOD PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
