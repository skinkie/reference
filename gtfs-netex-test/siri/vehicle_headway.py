from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class VehicleHeadway:
    distance_gap: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    distance_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
