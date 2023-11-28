from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.sales_offer_package_element import SalesOfferPackageElement
from netex.sales_offer_package_element_ref import SalesOfferPackageElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageElementsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SALES OFFER PACKAGE ELEMENTs.
    """
    class Meta:
        name = "salesOfferPackageElements_RelStructure"

    sales_offer_package_element_ref_or_sales_offer_package_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOfferPackageElementRef",
                    "type": SalesOfferPackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElement",
                    "type": SalesOfferPackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
