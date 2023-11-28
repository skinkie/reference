from dataclasses import dataclass
from netex.dynamic_stop_assignment_ref_structure import DynamicStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicStopAssignmentRef(DynamicStopAssignmentRefStructure):
    """
    Reference to a DYNAMIC STOP ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
