from dataclasses import dataclass
from netex.train_component_label_assignment_ref_structure import TrainComponentLabelAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponentLabelAssignmentRef(TrainComponentLabelAssignmentRefStructure):
    """
    Reference to a TRAIN COMPONENT NUMBER ASSIGNNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
