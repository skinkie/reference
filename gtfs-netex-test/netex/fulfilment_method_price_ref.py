from dataclasses import dataclass

from .fulfilment_method_price_ref_structure import FulfilmentMethodPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FulfilmentMethodPriceRef(FulfilmentMethodPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
