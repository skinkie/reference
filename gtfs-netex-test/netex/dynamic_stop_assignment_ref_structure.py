from dataclasses import dataclass

from .vehicle_journey_stop_assignment_ref_structure import VehicleJourneyStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignmentRefStructure(VehicleJourneyStopAssignmentRefStructure):
    pass
