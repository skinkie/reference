from dataclasses import dataclass

from .assignment_version_structure_2 import AssignmentVersionStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AssignmentVersionStructure1(AssignmentVersionStructure2):
    class Meta:
        name = "Assignment_VersionStructure"
