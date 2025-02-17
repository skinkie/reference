from dataclasses import dataclass

from .display_assignment_ref_structure import DisplayAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DisplayAssignmentRef(DisplayAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
