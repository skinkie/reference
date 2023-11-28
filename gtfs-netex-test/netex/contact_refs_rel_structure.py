from dataclasses import dataclass, field
from typing import List
from netex.contact_ref import ContactRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContactRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of REUSABLE CONTACT.

    +v1.2.2
    """
    class Meta:
        name = "contactRefs_RelStructure"

    contact_ref: List[ContactRef] = field(
        default_factory=list,
        metadata={
            "name": "ContactRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
