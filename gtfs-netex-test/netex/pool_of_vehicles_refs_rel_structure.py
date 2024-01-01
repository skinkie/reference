from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .pool_of_vehicles_ref import PoolOfVehiclesRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PoolOfVehiclesRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "PoolOfVehiclesRefs_RelStructure"

    pool_of_vehicles_ref: List[PoolOfVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "PoolOfVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
