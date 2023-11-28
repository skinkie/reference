from dataclasses import dataclass
from netex.controllable_element_price_ref_structure import ControllableElementPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementPriceRef(ControllableElementPriceRefStructure):
    """
    Reference to a CONTROLLABLE ELEMENT PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
