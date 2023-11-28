from dataclasses import dataclass
from netex.vehicle_journey_stop_assignment_ref_structure import VehicleJourneyStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyStopAssignmentRef(VehicleJourneyStopAssignmentRefStructure):
    """
    Reference to a VEHICLE JOURNEY STOP ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
