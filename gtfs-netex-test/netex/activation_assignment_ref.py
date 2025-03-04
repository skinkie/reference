from dataclasses import dataclass

from .activation_assignment_ref_structure import ActivationAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ActivationAssignmentRef(ActivationAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
