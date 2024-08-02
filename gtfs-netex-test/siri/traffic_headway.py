from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .traffic_value import TrafficValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TrafficHeadway(TrafficValue):
    average_distance_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "averageDistanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    average_time_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "averageTimeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
