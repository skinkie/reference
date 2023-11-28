from dataclasses import dataclass
from netex.passenger_stop_assignment_ref_structure import PassengerStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicStopAssignmentRefStructure(PassengerStopAssignmentRefStructure):
    """
    Type for a reference to a DYNAMIC STOP ASSIGNMENT.
    """
