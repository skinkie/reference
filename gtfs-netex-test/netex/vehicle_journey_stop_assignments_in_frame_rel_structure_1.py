from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_journey_stop_assignment import VehicleJourneyStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyStopAssignmentsInFrameRelStructure1(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE JOURNEY STOP ASSIGNMENTs.

    :ivar vehicle_journey_stop_assignment: The allocation of a SCHEDULED
        STOP POINT (i.e. a SCHEDULED STOP POINT of a SERVICE PATTERN or
        JOURNEY PATTERN) to a specific STOP PLACE or QUAY, for either a
        Passenger JOURNEY or VEHICLE SERVICE.
    """
    class Meta:
        name = "VehicleJourneyStopAssignmentsInFrame_RelStructure"

    vehicle_journey_stop_assignment: List[VehicleJourneyStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
