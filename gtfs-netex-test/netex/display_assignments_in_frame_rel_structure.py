from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.display_assignment import DisplayAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DisplayAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in DISPLAY ASSIGNMENTs.
    """
    class Meta:
        name = "displayAssignmentsInFrame_RelStructure"

    display_assignment: List[DisplayAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
