from dataclasses import dataclass, field

from .fleet_ref import FleetRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FleetRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fleetRefs_RelStructure"

    fleet_ref: list[FleetRef] = field(
        default_factory=list,
        metadata={
            "name": "FleetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
