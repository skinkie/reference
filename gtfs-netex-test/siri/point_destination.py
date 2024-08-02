from dataclasses import dataclass, field
from typing import Optional

from .destination_abstract import DestinationAbstract
from .extension_type import ExtensionType
from .point_1 import Point1

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class PointDestination(DestinationAbstract):
    point: Point1 = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    point_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
