from dataclasses import dataclass, field

from .point_on_route import PointOnRoute
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointsOnRouteRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pointsOnRoute_RelStructure"

    point_on_route: list[PointOnRoute] = field(
        default_factory=list,
        metadata={
            "name": "PointOnRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        },
    )
