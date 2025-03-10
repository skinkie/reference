from dataclasses import dataclass, field

from .crew_base_ref import CrewBaseRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CrewBaseRefsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "crewBaseRefs_RelStructure"

    crew_base_ref: list[CrewBaseRef] = field(
        default_factory=list,
        metadata={
            "name": "CrewBaseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
