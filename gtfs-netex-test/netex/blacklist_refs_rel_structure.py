from dataclasses import dataclass, field

from .blacklist_ref import BlacklistRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BlacklistRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "blacklistRefs_RelStructure"

    blacklist_ref: list[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
