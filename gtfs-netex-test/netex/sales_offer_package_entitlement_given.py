from dataclasses import dataclass, field
from netex.sales_offer_package_entitlement_given_version_structure import SalesOfferPackageEntitlementGivenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageEntitlementGiven(SalesOfferPackageEntitlementGivenVersionStructure):
    """
    A right to a SALES OFFER PACKAGE given by a SALES OFFER PACKAGE .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
