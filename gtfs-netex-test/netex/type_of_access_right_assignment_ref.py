from dataclasses import dataclass

from .type_of_access_right_assignment_ref_structure import TypeOfAccessRightAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfAccessRightAssignmentRef(TypeOfAccessRightAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
