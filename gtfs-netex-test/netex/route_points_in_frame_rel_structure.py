from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.route_point import RoutePoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutePointsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ROUTE POINT.
    """
    class Meta:
        name = "routePointsInFrame_RelStructure"

    route_point: List[RoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
