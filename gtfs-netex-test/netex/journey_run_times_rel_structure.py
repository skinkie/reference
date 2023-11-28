from dataclasses import dataclass, field
from typing import List
from netex.journey_run_time import JourneyRunTime
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyRunTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of JOURNEY RUN TIME.
    """
    class Meta:
        name = "journeyRunTimes_RelStructure"

    journey_run_time: List[JourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
