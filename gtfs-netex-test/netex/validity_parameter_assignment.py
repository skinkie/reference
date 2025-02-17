from dataclasses import dataclass

from .validity_parameter_assignment_version_structure import ValidityParameterAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidityParameterAssignment(ValidityParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
