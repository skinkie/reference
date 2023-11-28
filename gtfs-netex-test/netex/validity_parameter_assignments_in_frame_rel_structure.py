from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityParameterAssignmentsInFrameRelStructure(FrameContainmentStructure):
    """
    The assignment of a fare collection parameter (referring to geography, time,
    quality or usage) to an element of a fare system (access right, validated
    access, control mean, etc.).
    """
    class Meta:
        name = "validityParameterAssignmentsInFrame_RelStructure"

    validity_parameter_assignment: List[ValidityParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ValidityParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
