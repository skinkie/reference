from dataclasses import dataclass

from .sales_offer_package_substitution_ref_structure import SalesOfferPackageSubstitutionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesOfferPackageSubstitutionRef(SalesOfferPackageSubstitutionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
