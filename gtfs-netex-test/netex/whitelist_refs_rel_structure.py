from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WhitelistRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of WHITELISTs.
    """
    class Meta:
        name = "whitelistRefs_RelStructure"

    whitelist_ref: List[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
