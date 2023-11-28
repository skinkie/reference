from dataclasses import dataclass
from netex.sales_offer_package_ref_structure import SalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageRef(SalesOfferPackageRefStructure):
    """
    Reference to a SALES OFFER PACKAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
