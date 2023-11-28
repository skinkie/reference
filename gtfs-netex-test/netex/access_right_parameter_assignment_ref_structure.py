from dataclasses import dataclass
from netex.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightParameterAssignmentRefStructure(AssignmentRefStructure):
    """
    Type for Reference to an ACCESS RIGHT PARAMETER ASSIGNMENT.
    """
