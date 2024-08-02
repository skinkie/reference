from dataclasses import dataclass, field
from typing import Optional

from .alert_cpoint import AlertCpoint
from .extension_type import ExtensionType
from .network_location import NetworkLocation
from .point_by_coordinates import PointByCoordinates
from .roadside_reference_point import RoadsideReferencePoint
from .tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Point1(NetworkLocation):
    class Meta:
        name = "Point"

    tpeg_point_location: Optional[TpegPointLocation] = field(
        default=None,
        metadata={
            "name": "tpegPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_cpoint: Optional[AlertCpoint] = field(
        default=None,
        metadata={
            "name": "alertCPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point: Optional[RoadsideReferencePoint] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_by_coordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
