from dataclasses import dataclass

from .type_of_sales_offer_package_ref_structure import TypeOfSalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfSalesOfferPackageRef(TypeOfSalesOfferPackageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
