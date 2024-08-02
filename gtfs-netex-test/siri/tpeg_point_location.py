from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_loc02_direction_type_enum import TpegLoc02DirectionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegPointLocation:
    tpeg_direction: TpegLoc02DirectionTypeEnum = field(
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
