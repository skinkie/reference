from dataclasses import dataclass, field
from typing import List, Optional

from .conditions import Conditions
from .extension_type import ExtensionType
from .humidity import Humidity
from .pollution_measurement import PollutionMeasurement
from .poor_environment_type_enum import PoorEnvironmentTypeEnum
from .precipitation_detail import PrecipitationDetail
from .temperature import Temperature
from .visibility import Visibility
from .wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class PoorEnvironmentConditions(Conditions):
    poor_environment_type: List[PoorEnvironmentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pollution_measurement: List[PollutionMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "pollutionMeasurement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    poor_environment_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
