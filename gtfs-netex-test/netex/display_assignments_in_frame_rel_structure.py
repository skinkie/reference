from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .display_assignment import DisplayAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DisplayAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "displayAssignmentsInFrame_RelStructure"

    display_assignment: list[DisplayAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
