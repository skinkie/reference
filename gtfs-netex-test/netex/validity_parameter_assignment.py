from dataclasses import dataclass, field
from netex.validity_parameter_assignment_version_structure import ValidityParameterAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityParameterAssignment(ValidityParameterAssignmentVersionStructure):
    """
    An ACCESS RIGHT PARAMETER ASSIGNMENT relating a fare collection parameter to a
    theoretical FARE PRODUCT (or one of its components) or a SALES OFFER PACKAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
