from dataclasses import dataclass, field
from netex.vehicle_journey_stop_assignment_version_structure import VehicleJourneyStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyStopAssignment(VehicleJourneyStopAssignmentVersionStructure):
    """
    Change to a PASSENGER STOP ASSIGNMENT for a specific VEHICLE JOURNEY +v1.1.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
