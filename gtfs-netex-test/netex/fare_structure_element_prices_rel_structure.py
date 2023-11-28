from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.fare_structure_element_price_versioned_child_structure import FareStructureElementPriceVersionedChildStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE STRUCTURE ELEMENT PRICEs.
    """
    class Meta:
        name = "fareStructureElementPrices_RelStructure"

    fare_structure_element_price_ref_or_fare_structure_element_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPriceVersionedChildStructure,
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
