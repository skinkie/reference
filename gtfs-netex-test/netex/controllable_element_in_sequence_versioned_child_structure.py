from dataclasses import dataclass, field
from typing import Optional
from netex.access_right_parameter_assignments_rel_structure import AccessRightParameterAssignmentsRelStructure
from netex.controllable_element_ref import ControllableElementRef
from netex.fare_element_in_sequence_versioned_child_structure import FareElementInSequenceVersionedChildStructure
from netex.fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementInSequenceVersionedChildStructure(FareElementInSequenceVersionedChildStructure):
    """
    Type for CONTROLLABLE ELEMENT IN SEQUENCE.

    :ivar controllable_element_ref:
    :ivar fare_structure_element_ref:
    :ivar access_right_parameter_assignments: ACCESS RIGHT PARAMETER
        ASSIGNMENTs that apply to the VALIDABLE ELEMENT.
    """
    class Meta:
        name = "ControllableElementInSequence_VersionedChildStructure"

    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_parameter_assignments: Optional[AccessRightParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
