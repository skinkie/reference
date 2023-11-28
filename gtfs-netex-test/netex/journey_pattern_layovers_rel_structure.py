from dataclasses import dataclass, field
from typing import List
from netex.journey_pattern_layover import JourneyPatternLayover
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternLayoversRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of JOURNEY PATTERN LAYOVERs.

    :ivar journey_pattern_layover: JOURNEY PATTERN LAYOVER for a
        specified TIME DEMAND TYPE.
    """
    class Meta:
        name = "journeyPatternLayovers_RelStructure"

    journey_pattern_layover: List[JourneyPatternLayover] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
