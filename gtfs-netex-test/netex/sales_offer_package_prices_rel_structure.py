from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.sales_offer_package_price_versioned_child_structure import SalesOfferPackagePriceVersionedChildStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackagePricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of SALES OFFER PACKAGE PRICEs.
    """
    class Meta:
        name = "salesOfferPackagePrices_RelStructure"

    sales_offer_package_price_ref_or_sales_offer_package_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
