from dataclasses import dataclass, field
from typing import List
from netex.access_right_parameter_assignment import AccessRightParameterAssignment
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from netex.generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from netex.specific_parameter_assignment_version_structure import SpecificParameterAssignment
from netex.validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE ACCESS RIGHT PARAMETERs.
    """
    class Meta:
        name = "accessRightParameterAssignments_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchaseParameterAssignment",
                    "type": CustomerPurchaseParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecificParameterAssignment",
                    "type": SpecificParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignment",
                    "type": ValidityParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightParameterAssignment",
                    "type": AccessRightParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
