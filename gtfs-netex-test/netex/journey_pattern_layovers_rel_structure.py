from dataclasses import dataclass, field

from .journey_pattern_layover import JourneyPatternLayover
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPatternLayoversRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyPatternLayovers_RelStructure"

    journey_pattern_layover: list[JourneyPatternLayover] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
