from dataclasses import dataclass, field
from netex.train_component_label_assignment_version_structure import TrainComponentLabelAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponentLabelAssignment(TrainComponentLabelAssignmentVersionStructure):
    """
    The allocation of an advertised designation for a vehicle or vehicle element
    for passengers.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
