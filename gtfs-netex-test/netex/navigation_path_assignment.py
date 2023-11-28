from dataclasses import dataclass, field
from netex.navigation_path_assignment_version_structure import NavigationPathAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathAssignment(NavigationPathAssignmentVersionStructure):
    """
    Assignment of a CONNECTION link to a NAVIGATION PATH.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
