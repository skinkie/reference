from dataclasses import dataclass, field

from .distribution_assignment import DistributionAssignment
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DistributionAssignmentsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "distributionAssignmentsInFrame_RelStructure"

    distribution_assignment: list[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
