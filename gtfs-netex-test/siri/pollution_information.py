from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .pollution_measurement import PollutionMeasurement
from .weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class PollutionInformation(WeatherValue):
    pollution_measurement: List[PollutionMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "pollutionMeasurement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    pollution_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
