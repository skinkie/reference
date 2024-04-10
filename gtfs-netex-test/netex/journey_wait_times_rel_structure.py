from dataclasses import dataclass, field
from typing import List

from .journey_wait_time import JourneyWaitTime
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyWaitTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyWaitTimes_RelStructure"

    journey_wait_time: List[JourneyWaitTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
