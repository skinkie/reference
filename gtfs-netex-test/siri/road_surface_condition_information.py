from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .road_surface_condition_measurements import RoadSurfaceConditionMeasurements
from .weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadSurfaceConditionInformation(WeatherValue):
    road_surface_condition_measurements: RoadSurfaceConditionMeasurements = field(
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    road_surface_condition_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
