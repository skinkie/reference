from dataclasses import dataclass, field
from typing import List
from netex.cell_ref import CellRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CellRefsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE CELLs.
    """
    class Meta:
        name = "cellRefs_RelStructure"

    cell_ref: List[CellRef] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
