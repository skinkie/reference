from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfAccessRightAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF ACCESS RIGHT ASSIGNMENT.
    """
    class Meta:
        name = "TypeOfAccessRightAssignmentRefs_RelStructure"

    type_of_access_right_assignment_ref: List[TypeOfAccessRightAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
