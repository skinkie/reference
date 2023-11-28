from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.series_constraint_price_versioned_child_structure import SeriesConstraintPriceVersionedChildStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of SERIES CONSTRAINT PRICEs.
    """
    class Meta:
        name = "seriesConstraintPrices_RelStructure"

    series_constraint_price_ref_or_series_constraint_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPriceVersionedChildStructure,
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
