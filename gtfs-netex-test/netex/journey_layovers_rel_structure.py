from dataclasses import dataclass, field

from .journey_layover import JourneyLayover
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyLayoversRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyLayovers_RelStructure"

    journey_layover: list[JourneyLayover] = field(
        default_factory=list,
        metadata={
            "name": "JourneyLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
