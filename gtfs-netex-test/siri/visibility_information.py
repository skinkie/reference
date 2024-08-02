from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .visibility import Visibility
from .weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class VisibilityInformation(WeatherValue):
    visibility: Visibility = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    visibility_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
