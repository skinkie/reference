from dataclasses import dataclass

from .sales_offer_package_element_ref_structure import SalesOfferPackageElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesOfferPackageElementRef(SalesOfferPackageElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
