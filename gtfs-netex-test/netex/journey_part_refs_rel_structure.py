from dataclasses import dataclass, field
from typing import List
from netex.journey_part_ref import JourneyPartRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of JOURNEY PARTs.
    """
    class Meta:
        name = "journeyPartRefs_RelStructure"

    journey_part_ref: List[JourneyPartRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
