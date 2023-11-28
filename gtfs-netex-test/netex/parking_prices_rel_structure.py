from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.cell_versioned_child_structure import ParkingPriceVersionedChildStructure
from netex.parking_price_ref import ParkingPriceRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of PARKING TARIFF PRICEs.
    """
    class Meta:
        name = "parkingPrices_RelStructure"

    parking_price_ref_or_cell_ref_or_parking_price: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": ParkingPriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
