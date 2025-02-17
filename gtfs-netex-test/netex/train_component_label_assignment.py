from dataclasses import dataclass

from .train_component_label_assignment_version_structure import TrainComponentLabelAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainComponentLabelAssignment(TrainComponentLabelAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
