from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .temperature import Temperature
from .weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TemperatureInformation(WeatherValue):
    temperature: Temperature = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    temperature_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
