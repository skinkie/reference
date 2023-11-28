from dataclasses import dataclass, field
from netex.location_structure_2 import LocationStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BoundingBoxStructure2:
    """Defines a bounding box using two corner points.

    GML terminology.

    :ivar upper_left: A geospatial point. Upper Left corner. .
    :ivar lower_right: A geospatial point. Lower right corner. .
    """
    class Meta:
        name = "BoundingBoxStructure"

    upper_left: LocationStructure2 = field(
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    lower_right: LocationStructure2 = field(
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
