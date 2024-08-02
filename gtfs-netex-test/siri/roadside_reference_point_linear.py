from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .roadside_reference_point_primary_location import RoadsideReferencePointPrimaryLocation
from .roadside_reference_point_secondary_location import RoadsideReferencePointSecondaryLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadsideReferencePointLinear:
    roadside_reference_point_primary_location: RoadsideReferencePointPrimaryLocation = field(
        metadata={
            "name": "roadsideReferencePointPrimaryLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    roadside_reference_point_secondary_location: RoadsideReferencePointSecondaryLocation = field(
        metadata={
            "name": "roadsideReferencePointSecondaryLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    roadside_reference_point_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
