from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.pool_of_vehicles import PoolOfVehicles

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PoolOfVehiclesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a POOL OF VEHICLEs.

    :ivar pool_of_vehicles: A set of vehicles assigned to a specific
        PARKING, PARKING AREAs, PARKING BAYs, p lace  or MOBILITY
        CONSTRAINT ZONE that must be  picked up and returned to the same
        area. .  +v1.2.2
    """
    class Meta:
        name = "poolOfVehicles_RelStructure"

    pool_of_vehicles: List[PoolOfVehicles] = field(
        default_factory=list,
        metadata={
            "name": "PoolOfVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
