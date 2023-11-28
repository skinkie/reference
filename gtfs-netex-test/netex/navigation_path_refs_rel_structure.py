from dataclasses import dataclass, field
from typing import List
from netex.navigation_path_ref import NavigationPathRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a NAVIGATION PATH.
    """
    class Meta:
        name = "navigationPathRefs_RelStructure"

    navigation_path_ref: List[NavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
