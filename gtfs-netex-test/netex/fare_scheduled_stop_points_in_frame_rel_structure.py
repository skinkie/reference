from dataclasses import dataclass, field
from typing import List
from netex.fare_scheduled_stop_point import FareScheduledStopPoint
from netex.frame_containment_structure import FrameContainmentStructure
from netex.scheduled_stop_point import ScheduledStopPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareScheduledStopPointsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of  FARE SCHEUDLED STOP POINT.
    """
    class Meta:
        name = "fareScheduledStopPointsInFrame_RelStructure"

    scheduled_stop_point_or_fare_scheduled_stop_point: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
