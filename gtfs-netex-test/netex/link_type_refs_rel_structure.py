from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_link_ref import TypeOfLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF LINK.

    :ivar type_of_link_ref: Reference to a TYPE OF LINK.
    """
    class Meta:
        name = "linkTypeRefs_RelStructure"

    type_of_link_ref: List[TypeOfLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
