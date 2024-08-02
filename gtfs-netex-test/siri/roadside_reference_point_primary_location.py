from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .roadside_reference_point import RoadsideReferencePoint

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadsideReferencePointPrimaryLocation:
    roadside_reference_point: RoadsideReferencePoint = field(
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    roadside_reference_point_primary_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointPrimaryLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
