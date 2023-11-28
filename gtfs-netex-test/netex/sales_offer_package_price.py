from dataclasses import dataclass, field
from netex.sales_offer_package_price_versioned_child_structure import SalesOfferPackagePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackagePrice(SalesOfferPackagePriceVersionedChildStructure):
    """A set of all possible price features of a SALES OFFER PACKAGE ELEMENT: default total price, discount in value or percentage etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
