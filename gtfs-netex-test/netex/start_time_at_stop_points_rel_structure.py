from dataclasses import dataclass, field
from typing import Union

from .start_time_at_stop_point import StartTimeAtStopPoint
from .start_time_at_stop_point_ref import StartTimeAtStopPointRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StartTimeAtStopPointsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "startTimeAtStopPoints_RelStructure"

    start_time_at_stop_point_ref_or_start_time_at_stop_point: list[Union[StartTimeAtStopPointRef, StartTimeAtStopPoint]] = field(
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
        },
    )
