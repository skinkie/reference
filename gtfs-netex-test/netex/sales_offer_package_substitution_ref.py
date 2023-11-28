from dataclasses import dataclass
from netex.sales_offer_package_substitution_ref_structure import SalesOfferPackageSubstitutionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageSubstitutionRef(SalesOfferPackageSubstitutionRefStructure):
    """
    Reference to a SALES OFFER PACKAGE SUBSTITUTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
