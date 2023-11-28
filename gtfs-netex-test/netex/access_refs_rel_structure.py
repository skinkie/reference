from dataclasses import dataclass, field
from typing import List
from netex.access_ref import AccessRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to an ACCESS link.
    """
    class Meta:
        name = "accessRefs_RelStructure"

    access_ref: List[AccessRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
