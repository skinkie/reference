from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_height import TpegHeight
from .tpeg_loc01_area_location_subtype_enum import TpegLoc01AreaLocationSubtypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegAreaLocation:
    tpeg_area_location_type: TpegLoc01AreaLocationSubtypeEnum = field(
        metadata={
            "name": "tpegAreaLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_height: Optional[TpegHeight] = field(
        default=None,
        metadata={
            "name": "tpegHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
