from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .vehicle_journey_wait_time import VehicleJourneyWaitTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleJourneyWaitTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyWaitTimes_RelStructure"

    vehicle_journey_wait_time: list[VehicleJourneyWaitTime] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
