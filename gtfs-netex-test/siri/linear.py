from dataclasses import dataclass, field
from typing import Optional

from .alert_clinear import AlertClinear
from .extension_type import ExtensionType
from .network_location import NetworkLocation
from .roadside_reference_point_linear import RoadsideReferencePointLinear
from .tpeg_linear_location import TpegLinearLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Linear(NetworkLocation):
    tpeg_linear_location: Optional[TpegLinearLocation] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_clinear: Optional[AlertClinear] = field(
        default=None,
        metadata={
            "name": "alertCLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point_linear: Optional[RoadsideReferencePointLinear] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
