from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.price_unit import PriceUnit
from netex.price_unit_ref import PriceUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PriceUnitsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PRICE UNITs.
    """
    class Meta:
        name = "priceUnits_RelStructure"

    price_unit_ref_or_price_unit: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PriceUnitRef",
                    "type": PriceUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnit",
                    "type": PriceUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
