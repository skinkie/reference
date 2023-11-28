from dataclasses import dataclass, field
from typing import List
from netex.blacklist_ref import BlacklistRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SecuritylistRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of SECURITY LIST.s.
    """
    class Meta:
        name = "securitylistRefs_RelStructure"

    whitelist_ref_or_blacklist_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
