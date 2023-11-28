from dataclasses import dataclass
from netex.passenger_stop_assignment_ref_structure import PassengerStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerStopAssignmentRef(PassengerStopAssignmentRefStructure):
    """
    Reference to a PASSENGER STOP ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
