from dataclasses import dataclass, field

from .mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MobilityServiceConstraintZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "mobilityServiceConstraintZoneRefs_RelStructure"

    mobility_service_constraint_zone_ref: list[MobilityServiceConstraintZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "MobilityServiceConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
