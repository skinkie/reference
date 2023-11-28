from dataclasses import dataclass
from netex.group_of_sales_offer_packages_ref_structure import GroupOfSalesOfferPackagesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfSalesOfferPackagesRef(GroupOfSalesOfferPackagesRefStructure):
    """
    Reference to a GROUP OF SALES OFFER PACKAGEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
