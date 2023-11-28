from dataclasses import dataclass, field
from netex.dynamic_stop_assignment_version_structure import DynamicStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicStopAssignment(DynamicStopAssignmentVersionStructure):
    """
    Change to a PASSENGER STOP ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
