from dataclasses import dataclass, field
from typing import List
from netex.point_1 import Point1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class PointArrayPropertyType:
    """Gml:PointArrayPropertyType is a container for an array of points.

    The elements are always contained inline in the array property,
    referencing geometry elements or arrays of geometry elements via
    XLinks is not supported.
    """
    point: List[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
