from dataclasses import dataclass, field
from typing import List
from netex.line_string import LineString
from netex.point_1 import Point1
from netex.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class GeometryArrayPropertyType:
    """If a feature has a property which takes an array of geometry elements as its
    value, this is called a geometry array property.

    A generic type for such a geometry property is
    GeometryArrayPropertyType. The elements are always contained inline
    in the array property, referencing geometry elements or arrays of
    geometry elements via XLinks is not supported.
    """
    polygon_or_line_string_or_point: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "Point",
                    "type": Point1,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
