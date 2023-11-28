from dataclasses import dataclass, field
from netex.flexible_stop_assignment_version_structure import FlexibleStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleStopAssignment(FlexibleStopAssignmentVersionStructure):
    """Assignment of a SCHEDULED STOP POINT to a FLEXIBLE STOP PLACE and quay.

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
