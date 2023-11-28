from dataclasses import dataclass
from netex.train_stop_assignment_ref_structure import TrainStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainStopAssignmentRef(TrainStopAssignmentRefStructure):
    """
    Reference to a TRAIN STOP ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
