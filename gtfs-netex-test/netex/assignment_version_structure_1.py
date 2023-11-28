from dataclasses import dataclass
from netex.assignment_version_structure_2 import AssignmentVersionStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssignmentVersionStructure1(AssignmentVersionStructure2):
    """
    Type for  ASSIGNMENT.
    """
    class Meta:
        name = "Assignment_VersionStructure"
