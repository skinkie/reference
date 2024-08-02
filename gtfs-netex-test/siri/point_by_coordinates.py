from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class PointByCoordinates:
    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_coordinates: PointCoordinates = field(
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    point_by_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
