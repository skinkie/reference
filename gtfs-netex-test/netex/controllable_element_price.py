from dataclasses import dataclass

from .controllable_element_price_versioned_child_structure import ControllableElementPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ControllableElementPrice(ControllableElementPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
