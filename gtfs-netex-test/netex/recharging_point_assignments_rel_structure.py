from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .recharging_point_assignment import RechargingPointAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RechargingPointAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "rechargingPointAssignments_RelStructure"

    recharging_point_assignment: list[RechargingPointAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RechargingPointAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
