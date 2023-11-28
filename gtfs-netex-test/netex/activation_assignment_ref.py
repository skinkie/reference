from dataclasses import dataclass
from netex.activation_assignment_ref_structure import ActivationAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationAssignmentRef(ActivationAssignmentRefStructure):
    """
    Reference to an ACTIVATION ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
