from dataclasses import dataclass, field
from netex.sales_offer_package_entitlement_required_version_structure import SalesOfferPackageEntitlementRequiredVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageEntitlementRequired(SalesOfferPackageEntitlementRequiredVersionStructure):
    """
    A rerirement to a SALES OFFER PACKAGE  in order to purchase or use PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
