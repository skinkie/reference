from dataclasses import dataclass
from netex.validity_parameter_assignment_ref_structure import ValidityParameterAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GenericParameterAssignmentRefStructure(ValidityParameterAssignmentRefStructure):
    """
    Type for Reference to a GENERIC PARAMETER.
    """
