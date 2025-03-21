from dataclasses import dataclass, field

from .mode_ref import ModeRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ModeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "modeRefs_RelStructure"

    mode_ref: list[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "ModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
