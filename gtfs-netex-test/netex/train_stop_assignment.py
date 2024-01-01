from dataclasses import dataclass
from .train_stop_assignment_version_structure import (
    TrainStopAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainStopAssignment(TrainStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
