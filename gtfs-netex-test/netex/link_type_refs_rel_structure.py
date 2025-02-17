from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_link_ref import TypeOfLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinkTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "linkTypeRefs_RelStructure"

    type_of_link_ref: list[TypeOfLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
