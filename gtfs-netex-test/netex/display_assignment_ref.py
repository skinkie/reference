from dataclasses import dataclass
from netex.display_assignment_ref_structure import DisplayAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DisplayAssignmentRef(DisplayAssignmentRefStructure):
    """
    Reference to a DISPLAY ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
