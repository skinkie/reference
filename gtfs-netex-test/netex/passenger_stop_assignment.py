from dataclasses import dataclass, field
from netex.passenger_stop_assignment_version_structure import PassengerStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerStopAssignment(PassengerStopAssignmentVersionStructure):
    """Assignment of a SCHEDULED STOP POINT to a STOP PLACE and QUAY, etc..

    For associations to ZONE see FlexibleStopAssignment.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
