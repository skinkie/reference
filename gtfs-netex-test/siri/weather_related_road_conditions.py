from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .road_conditions import RoadConditions
from .road_surface_condition_measurements import RoadSurfaceConditionMeasurements
from .weather_related_road_condition_type_enum import WeatherRelatedRoadConditionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class WeatherRelatedRoadConditions(RoadConditions):
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
