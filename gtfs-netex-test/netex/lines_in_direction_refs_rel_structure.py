from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.line_in_direction_ref import LineInDirectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinesInDirectionRefsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LINE in a specific DIRECTION.
    """
    class Meta:
        name = "linesInDirectionRefs_RelStructure"

    line_in_direction_ref: List[LineInDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineInDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
