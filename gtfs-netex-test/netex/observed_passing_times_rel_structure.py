from dataclasses import dataclass, field

from .observed_passing_time import ObservedPassingTime
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ObservedPassingTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "observedPassingTimes_RelStructure"

    observed_passing_time: list[ObservedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "ObservedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
