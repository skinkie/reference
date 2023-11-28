from dataclasses import dataclass, field
from typing import List
from netex.access_right_parameter_assignment import AccessRightParameterAssignment
from netex.customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from netex.frame_containment_structure import FrameContainmentStructure
from netex.generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from netex.specific_parameter_assignment_version_structure import SpecificParameterAssignment
from netex.validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightParameterAssignmentsInFrameRelStructure(FrameContainmentStructure):
    """
    The assignment of a fare collection parameter (referring to geography, time,
    quality or usage) to an element of a fare system (access right, validated
    access, control mean, etc.).
    """
    class Meta:
        name = "accessRightParameterAssignmentsInFrame_RelStructure"

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
