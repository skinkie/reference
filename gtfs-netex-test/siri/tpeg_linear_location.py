from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_loc01_linear_location_subtype_enum import TpegLoc01LinearLocationSubtypeEnum
from .tpeg_loc02_direction_type_enum import TpegLoc02DirectionTypeEnum
from .tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegLinearLocation:
    tpeg_direction: TpegLoc02DirectionTypeEnum = field(
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_linear_location_type: TpegLoc01LinearLocationSubtypeEnum = field(
        metadata={
            "name": "tpegLinearLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    to: TpegPoint = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    from_value: TpegPoint = field(
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
