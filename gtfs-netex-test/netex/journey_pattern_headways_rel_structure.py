from dataclasses import dataclass, field
from typing import List
from netex.journey_pattern_headway import JourneyPatternHeadway
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternHeadwaysRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of JOURNEY PATTERN HEADWAYs.
    """
    class Meta:
        name = "journeyPatternHeadways_RelStructure"

    journey_pattern_headway: List[JourneyPatternHeadway] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
