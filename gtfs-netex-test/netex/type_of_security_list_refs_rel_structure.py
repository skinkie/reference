from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_security_list_ref import TypeOfSecurityListRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfSecurityListRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF SECURITY LIST.
    """
    class Meta:
        name = "typeOfSecurityListRefs_RelStructure"

    type_of_security_list_ref: List[TypeOfSecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
