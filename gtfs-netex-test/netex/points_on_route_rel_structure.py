from dataclasses import dataclass, field
from typing import List
from netex.point_on_route import PointOnRoute
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointsOnRouteRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of POINTs ON ROUTE.
    """
    class Meta:
        name = "pointsOnRoute_RelStructure"

    point_on_route: List[PointOnRoute] = field(
        default_factory=list,
        metadata={
            "name": "PointOnRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
