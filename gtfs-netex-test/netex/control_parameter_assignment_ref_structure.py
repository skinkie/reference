from dataclasses import dataclass

from .access_right_parameter_assignment_ref_structure import AccessRightParameterAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControlParameterAssignmentRefStructure(AccessRightParameterAssignmentRefStructure):
    pass
