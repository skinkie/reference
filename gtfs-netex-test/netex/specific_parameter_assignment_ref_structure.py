from dataclasses import dataclass
from netex.validity_parameter_assignment_ref_structure import ValidityParameterAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecificParameterAssignmentRefStructure(ValidityParameterAssignmentRefStructure):
    """
    Type for Reference to a SPECIFIC PARAMETER ASIGNMENT..
    """
