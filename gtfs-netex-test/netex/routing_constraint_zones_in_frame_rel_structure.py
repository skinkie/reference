from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .routing_constraint_zone import RoutingConstraintZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoutingConstraintZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routingConstraintZonesInFrame_RelStructure"

    routing_constraint_zone: list[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
