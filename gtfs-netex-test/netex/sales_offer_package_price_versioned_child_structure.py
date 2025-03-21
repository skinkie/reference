from dataclasses import dataclass, field
from typing import Optional, Union

from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .sales_offer_package_element_ref import SalesOfferPackageElementRef
from .sales_offer_package_ref import SalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesOfferPackagePriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "SalesOfferPackagePrice_VersionedChildStructure"

    sales_offer_package_ref_or_sales_offer_package_element_ref: Optional[Union[SalesOfferPackageRef, SalesOfferPackageElementRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElementRef",
                    "type": SalesOfferPackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
