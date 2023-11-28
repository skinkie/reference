from dataclasses import dataclass, field
from typing import List
from netex.mode_ref import ModeRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TRANSPORT MODEs.
    """
    class Meta:
        name = "modeRefs_RelStructure"

    mode_ref: List[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "ModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
