from dataclasses import dataclass, field
from typing import List, Union

from .line_string import LineString
from .point import Point
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class GeometryArrayPropertyType:
    abstract_surface_or_abstract_curve_or_abstract_geometric_primitive: List[Union[Polygon, LineString, Point]] = field(
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
                    "type": Point,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
