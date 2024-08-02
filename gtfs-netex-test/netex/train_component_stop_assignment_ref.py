from dataclasses import dataclass

from .train_component_stop_assignment_ref_structure import TrainComponentStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentStopAssignmentRef(TrainComponentStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
