from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.scheduled_stop_point import ScheduledStopPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SCHEDULED STOP POINTs.
    """
    class Meta:
        name = "scheduledStopPointsInFrame_RelStructure"

    scheduled_stop_point: List[ScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
