from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .point_coordinates import PointCoordinates
from .tpeg_area_descriptor import TpegAreaDescriptor
from .tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegGeometricArea(TpegAreaLocation):
    radius: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    centre_point: PointCoordinates = field(
        metadata={
            "name": "centrePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    name: Optional[TpegAreaDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_geometric_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegGeometricAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
