from dataclasses import dataclass, field
from netex.location_structure_1 import LocationStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class BoundingBoxStructure1:
    """Defines a bounding box using two corner points.

    GML terminology.  +SIRI v2.0

    :ivar upper_left: A geospatial point. Upper Left corner. .
    :ivar lower_right: A geospatial point. Lower right corner. .
    """
    class Meta:
        name = "BoundingBoxStructure"

    upper_left: LocationStructure1 = field(
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    lower_right: LocationStructure1 = field(
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
