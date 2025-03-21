from dataclasses import dataclass

from .controllable_element_price_ref_structure import ControllableElementPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ControllableElementPriceRef(ControllableElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
