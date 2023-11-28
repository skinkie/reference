from dataclasses import dataclass, field
from typing import List
from netex.point_in_journey_pattern import PointInJourneyPattern
from netex.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.timing_point_in_journey_pattern import TimingPointInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointsInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    """
    Type for POINT IN JOURNEY PATTERN.
    """
    class Meta:
        name = "pointsInJourneyPattern_RelStructure"

    point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointInJourneyPattern",
                    "type": PointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPattern",
                    "type": StopPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPattern",
                    "type": TimingPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 2,
        }
    )
