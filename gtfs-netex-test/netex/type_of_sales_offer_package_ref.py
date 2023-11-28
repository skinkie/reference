from dataclasses import dataclass
from netex.type_of_sales_offer_package_ref_structure import TypeOfSalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfSalesOfferPackageRef(TypeOfSalesOfferPackageRefStructure):
    """
    Reference to a TYPE OF SALES OFFER PACKAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
