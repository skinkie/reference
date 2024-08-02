from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_loc01_simple_point_location_subtype_enum import TpegLoc01SimplePointLocationSubtypeEnum
from .tpeg_point import TpegPoint
from .tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegSimplePoint(TpegPointLocation):
    tpeg_simple_point_location_type: TpegLoc01SimplePointLocationSubtypeEnum = field(
        metadata={
            "name": "tpegSimplePointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    point: TpegPoint = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_simple_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegSimplePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
