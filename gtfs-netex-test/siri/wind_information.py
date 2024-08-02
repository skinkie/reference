from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .weather_value import WeatherValue
from .wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class WindInformation(WeatherValue):
    wind: Wind = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    wind_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
