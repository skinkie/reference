from dataclasses import dataclass, field
from typing import List
from netex.fleet_ref import FleetRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FleetRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of FLEETs.
    """
    class Meta:
        name = "fleetRefs_RelStructure"

    fleet_ref: List[FleetRef] = field(
        default_factory=list,
        metadata={
            "name": "FleetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
