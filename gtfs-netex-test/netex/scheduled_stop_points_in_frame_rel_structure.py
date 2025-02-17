from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .scheduled_stop_point import ScheduledStopPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ScheduledStopPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "scheduledStopPointsInFrame_RelStructure"

    scheduled_stop_point: list[ScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
