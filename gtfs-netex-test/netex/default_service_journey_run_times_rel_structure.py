from dataclasses import dataclass, field
from typing import List
from netex.default_service_journey_run_time import DefaultServiceJourneyRunTime
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultServiceJourneyRunTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of properties of DEFAULT SERVICE JOURNEY / RUN TIME.

    :ivar default_service_journey_run_time: DEFAULT SERVICE JOURNEY /
        RUN TIME for a specified TIME DEMAND TYPE.
    """
    class Meta:
        name = "defaultServiceJourneyRunTimes_RelStructure"

    default_service_journey_run_time: List[DefaultServiceJourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "DefaultServiceJourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
