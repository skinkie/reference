from dataclasses import dataclass, field

from .boarding_position_ref import BoardingPositionRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BoardingPositionRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "boardingPositionRefs_RelStructure"

    boarding_position_ref: list[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
