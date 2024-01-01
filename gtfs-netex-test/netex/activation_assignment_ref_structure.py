from dataclasses import dataclass
from .assignment_ref_structure import AssignmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationAssignmentRefStructure(AssignmentRefStructure):
    value: RestrictedVar
