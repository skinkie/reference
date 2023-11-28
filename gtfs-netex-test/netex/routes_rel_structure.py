from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.route import Route
from netex.route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ROUTEs.
    """
    class Meta:
        name = "routes_RelStructure"

    route_ref_or_route: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Route",
                    "type": Route,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
