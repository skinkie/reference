from dataclasses import dataclass
from netex.stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleServiceAssignmentRefStructure(StopAssignmentRefStructure):
    """
    Type for a reference to a FLEXIBLE SERVICE ASSIGNMENT.
    """
