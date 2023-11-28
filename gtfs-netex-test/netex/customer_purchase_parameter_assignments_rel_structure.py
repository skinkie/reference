from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchaseParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMER PURCHASE PARAMETER ASSIGNMENT.

    :ivar customer_purchase_parameter_assignment: A VALIDITY PARAMETER
        ASSIGNMENT specifying practical parameters for a CUSTOMER
        PURCHASE PACKAGE, chosen from those available for a given fare
        structure (e.g. the origin or destination zone in a zone-
        counting system).
    """
    class Meta:
        name = "customerPurchaseParameterAssignments_RelStructure"

    customer_purchase_parameter_assignment: List[CustomerPurchaseParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchaseParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
