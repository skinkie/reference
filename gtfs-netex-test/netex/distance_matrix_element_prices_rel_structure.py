from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of DISTANCE MATRIX ELEMENT PRICEs.
    """
    class Meta:
        name = "distanceMatrixElementPrices_RelStructure"

    distance_matrix_element_price_ref_or_distance_matrix_element_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
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
