from dataclasses import dataclass
from .fare_price_ref_structure import FarePriceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackagePriceRefStructure(FarePriceRefStructure):
    value: RestrictedVar
