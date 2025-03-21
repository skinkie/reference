from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .sales_offer_package_element import SalesOfferPackageElement
from .sales_offer_package_element_ref import SalesOfferPackageElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesOfferPackageElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "salesOfferPackageElements_RelStructure"

    sales_offer_package_element_ref_or_sales_offer_package_element: list[Union[SalesOfferPackageElementRef, SalesOfferPackageElement]] = field(
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
        },
    )
