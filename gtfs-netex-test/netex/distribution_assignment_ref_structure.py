from dataclasses import dataclass
from netex.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistributionAssignmentRefStructure(AssignmentRefStructure):
    """
    Type for Reference to a DISTRIBUTION ASSIGNMENT.
    """
