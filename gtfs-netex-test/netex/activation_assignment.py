from dataclasses import dataclass
from .activation_assignment_version_structure import (
    ActivationAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationAssignment(ActivationAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
