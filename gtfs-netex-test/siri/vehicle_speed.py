from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class VehicleSpeed:
    individual_vehicle_speed: float = field(
        metadata={
            "name": "individualVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    vehicle_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
