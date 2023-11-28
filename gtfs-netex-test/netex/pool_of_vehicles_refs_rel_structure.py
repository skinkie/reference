from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.pool_of_vehicles_ref import PoolOfVehiclesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PoolOfVehiclesRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of POOL OF VEHICLEs.
    """
    class Meta:
        name = "PoolOfVehiclesRefs_RelStructure"

    pool_of_vehicles_ref: List[PoolOfVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "PoolOfVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
