from dataclasses import dataclass

from .fare_structure_element_price_ref_structure import FareStructureElementPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareStructureElementPriceRef(FareStructureElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
