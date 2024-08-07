from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .speed_percentile import SpeedPercentile
from .traffic_value import TrafficValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TrafficSpeed(TrafficValue):
    average_vehicle_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "averageVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    speed_percentile: Optional[SpeedPercentile] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
