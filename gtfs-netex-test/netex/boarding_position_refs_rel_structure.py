from dataclasses import dataclass, field
from typing import List
from netex.boarding_position_ref import BoardingPositionRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BoardingPositionRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a BOARDING POSITION.
    """
    class Meta:
        name = "boardingPositionRefs_RelStructure"

    boarding_position_ref: List[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
