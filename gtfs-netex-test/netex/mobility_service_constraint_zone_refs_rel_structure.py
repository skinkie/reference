from dataclasses import dataclass, field
from typing import List
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZoneRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of MOBILITY SERVICE CONSTRAINT ZONEs.
    """
    class Meta:
        name = "mobilityServiceConstraintZoneRefs_RelStructure"

    mobility_service_constraint_zone_ref: List[MobilityServiceConstraintZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "MobilityServiceConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
