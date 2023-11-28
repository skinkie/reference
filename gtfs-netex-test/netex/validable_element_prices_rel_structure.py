from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.validable_element_price import ValidableElementPrice
from netex.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidableElementPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of VALIDABLE ELEMENT PRICEs.
    """
    class Meta:
        name = "validableElementPrices_RelStructure"

    validable_element_price_ref_or_validable_element_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
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
