from dataclasses import dataclass
from netex.flexible_service_assignment_ref_structure import FlexibleServiceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleServiceAssignmentRef(FlexibleServiceAssignmentRefStructure):
    """
    Reference to a FLEXIBLE SERVICE ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
