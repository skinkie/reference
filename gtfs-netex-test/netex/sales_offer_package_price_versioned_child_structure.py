from dataclasses import dataclass, field
from typing import Optional
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.sales_offer_package_ref import SalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackagePriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a SALES OFFER PACKAGE PRICEs.
    """
    class Meta:
        name = "SalesOfferPackagePrice_VersionedChildStructure"

    sales_offer_package_ref_or_sales_offer_package_element_ref: Optional[object] = field(
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
        }
    )
