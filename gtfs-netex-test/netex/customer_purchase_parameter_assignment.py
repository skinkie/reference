from dataclasses import dataclass, field
from netex.customer_purchase_parameter_assignment_version_structure import CustomerPurchaseParameterAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchaseParameterAssignment(CustomerPurchaseParameterAssignmentVersionStructure):
    """
    A VALIDITY PARAMETER ASSIGNMENT specifying practical parameters for use in a
    CUSTOMER PURCHASE PACKAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
