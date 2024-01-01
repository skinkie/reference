from dataclasses import dataclass
from .activation_assignment_ref_structure import (
    ActivationAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationAssignmentRef(ActivationAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
