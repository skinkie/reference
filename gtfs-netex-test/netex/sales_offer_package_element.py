from dataclasses import dataclass

from .sales_offer_package_element_version_structure import SalesOfferPackageElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageElement(SalesOfferPackageElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
