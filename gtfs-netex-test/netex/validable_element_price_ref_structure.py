from dataclasses import dataclass

from .fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidableElementPriceRefStructure(FarePriceRefStructure):
    pass
