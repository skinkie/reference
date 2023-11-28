from dataclasses import dataclass
from netex.sales_offer_package_entitlement_required_ref_structure import SalesOfferPackageEntitlementRequiredRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageEntitlementRequiredRef(SalesOfferPackageEntitlementRequiredRefStructure):
    """
    Reference to a SALES OFFER ENTITLEMENT REQUIRED parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
