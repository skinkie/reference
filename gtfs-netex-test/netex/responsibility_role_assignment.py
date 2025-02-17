from dataclasses import dataclass

from .responsibility_role_assignment_versioned_child_structure import ResponsibilityRoleAssignmentVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ResponsibilityRoleAssignment(ResponsibilityRoleAssignmentVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
