from dataclasses import dataclass

from .stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainStopAssignmentRefStructure(StopAssignmentRefStructure):
    pass
