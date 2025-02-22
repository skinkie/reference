from dataclasses import dataclass, field

from .contact_ref import ContactRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ContactRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "contactRefs_RelStructure"

    contact_ref: list[ContactRef] = field(
        default_factory=list,
        metadata={
            "name": "ContactRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
