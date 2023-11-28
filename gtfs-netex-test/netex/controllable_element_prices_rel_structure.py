from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.controllable_element_price import ControllableElementPrice
from netex.controllable_element_price_ref import ControllableElementPriceRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CONTROLLABLE ELEMENT PRICEs.
    """
    class Meta:
        name = "controllableElementPrices_RelStructure"

    controllable_element_price_ref_or_cell_ref_or_controllable_element_price: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
