from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .obstruction import Obstruction
from .vehicle import Vehicle
from .vehicle_obstruction_type_enum import VehicleObstructionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class VehicleObstruction(Obstruction):
    vehicle_obstruction_type: VehicleObstructionTypeEnum = field(
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    obstructing_vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
