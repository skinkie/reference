from dataclasses import dataclass, field
from netex.train_stop_assignment_version_structure import TrainStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainStopAssignment(TrainStopAssignmentVersionStructure):
    """Assignment of a scheduled train stop point to a STOP PLACE and quay.

    etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
