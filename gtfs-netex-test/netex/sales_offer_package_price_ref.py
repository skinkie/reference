from dataclasses import dataclass
from .sales_offer_package_price_ref_structure import (
    SalesOfferPackagePriceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackagePriceRef(SalesOfferPackagePriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
