from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.vehicle_journey_run_time import VehicleJourneyRunTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyRunTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of VEHICLE JOURNEY RUN TIMEs.

    :ivar vehicle_journey_run_time: VEHICLE JOURNEY RUN TIME for a
        specified TIME DEMAND TYPE.
    """
    class Meta:
        name = "vehicleJourneyRunTimes_RelStructure"

    vehicle_journey_run_time: List[VehicleJourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
