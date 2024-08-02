from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class SpeedPercentile:
    vehicle_percentage: float = field(
        metadata={
            "name": "vehiclePercentage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    speed_percentile: float = field(
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    speed_percentile_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedPercentileExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
