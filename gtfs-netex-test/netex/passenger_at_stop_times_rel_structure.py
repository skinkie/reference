from dataclasses import dataclass, field
from typing import List

from .passenger_at_stop_time import PassengerAtStopTime
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerAtStopTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "passengerAtStopTimes_RelStructure"

    passenger_at_stop_time: List[PassengerAtStopTime] = field(
        default_factory=list,
        metadata={
            "name": "PassengerAtStopTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
