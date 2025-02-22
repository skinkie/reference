from dataclasses import dataclass

from .activation_assignment_version_structure import ActivationAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ActivationAssignment(ActivationAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
