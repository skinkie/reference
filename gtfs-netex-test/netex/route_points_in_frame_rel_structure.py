from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .route_point import RoutePoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoutePointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routePointsInFrame_RelStructure"

    route_point: list[RoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
