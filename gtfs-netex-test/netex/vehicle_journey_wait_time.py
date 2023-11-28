from dataclasses import dataclass, field
from netex.vehicle_journey_wait_time_versioned_child_structure import VehicleJourneyWaitTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyWaitTime(VehicleJourneyWaitTimeVersionedChildStructure):
    """The time for a vehicle to wait at a particular TIMING POINT IN JOURNEY
    PATTERN on a specified VEHICLE JOURNEY.

    This wait time will override the JOURNEY PATTERN WAIT TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
