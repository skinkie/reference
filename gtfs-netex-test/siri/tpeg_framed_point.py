from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_loc01_framed_point_location_subtype_enum import TpegLoc01FramedPointLocationSubtypeEnum
from .tpeg_non_junction_point import TpegNonJunctionPoint
from .tpeg_point import TpegPoint
from .tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegFramedPoint(TpegPointLocation):
    tpeg_framed_point_location_type: TpegLoc01FramedPointLocationSubtypeEnum = field(
        metadata={
            "name": "tpegFramedPointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    framed_point: TpegNonJunctionPoint = field(
        metadata={
            "name": "framedPoint",
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
    tpeg_framed_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
