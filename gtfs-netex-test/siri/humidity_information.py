from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .humidity import Humidity
from .weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class HumidityInformation(WeatherValue):
    humidity: Humidity = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    humidity_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
