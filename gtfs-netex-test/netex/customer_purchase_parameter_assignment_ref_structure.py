from dataclasses import dataclass

from .validity_parameter_assignment_ref_structure import ValidityParameterAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerPurchaseParameterAssignmentRefStructure(ValidityParameterAssignmentRefStructure):
    pass
