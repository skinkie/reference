from dataclasses import dataclass, field
from typing import List
from netex.start_time_at_stop_point import StartTimeAtStopPoint
from netex.start_time_at_stop_point_ref import StartTimeAtStopPointRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StartTimeAtStopPointsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of START TIME AT STOP POINT.
    """
    class Meta:
        name = "startTimeAtStopPoints_RelStructure"

    start_time_at_stop_point_ref_or_start_time_at_stop_point: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartTimeAtStopPointRef",
                    "type": StartTimeAtStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTimeAtStopPoint",
                    "type": StartTimeAtStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
