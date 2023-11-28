from dataclasses import dataclass
from netex.sales_offer_package_price_ref_structure import SalesOfferPackagePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackagePriceRef(SalesOfferPackagePriceRefStructure):
    """
    Reference to a SALES OFFER PACKAGE PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
