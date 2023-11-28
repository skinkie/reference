from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.fare_product_price import FareProductPrice
from netex.fare_product_price_ref import FareProductPriceRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE PRODUCT PRICEs.
    """
    class Meta:
        name = "fareProductPrices_RelStructure"

    fare_product_price_ref_or_cell_ref_or_fare_product_price: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
