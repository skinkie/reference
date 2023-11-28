from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.route_link import RouteLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteLinksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ROUTE LINK.
    """
    class Meta:
        name = "routeLinksInFrame_RelStructure"

    route_link: List[RouteLink] = field(
        default_factory=list,
        metadata={
            "name": "RouteLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
