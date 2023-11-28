from dataclasses import dataclass
from netex.passenger_stop_assignment_ref_structure import PassengerStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyStopAssignmentRefStructure(PassengerStopAssignmentRefStructure):
    """
    Type for a reference to a VEHICLE JOURNEY STOP ASSIGNMENT.
    """
