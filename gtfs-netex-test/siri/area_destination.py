from dataclasses import dataclass, field
from typing import Optional

from .area import Area
from .destination_abstract import DestinationAbstract
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AreaDestination(DestinationAbstract):
    area: Area = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    area_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
