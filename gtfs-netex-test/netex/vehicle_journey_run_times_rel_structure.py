from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .vehicle_journey_run_time import VehicleJourneyRunTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleJourneyRunTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyRunTimes_RelStructure"

    vehicle_journey_run_time: list[VehicleJourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
