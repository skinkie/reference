from dataclasses import dataclass
from netex.vehicle_journey_run_time_versioned_child_structure import VehicleJourneyRunTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyRunTime(VehicleJourneyRunTimeVersionedChildStructure):
    """The time taken to traverse a specified TIMING LINK IN JOURNEY PATTERN on a
    specified VEHICLE JOURNEY.

    This gives the most detailed control over times and overrides the
    DEFAULT SERVICE JOURNEY RUN TIME and JOURNEY PATTERN RUN TIME and
    the DEFAULT DEAD RUN RUN TIME. There may be different times for
    different TIME DEMAND TYPES.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
