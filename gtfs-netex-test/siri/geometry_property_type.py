from dataclasses import dataclass, field
from typing import Optional, Union

from .line_string import LineString
from .nil_reason_enumeration_value import NilReasonEnumerationValue
from .point import Point
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class GeometryPropertyType:
    abstract_surface_or_abstract_curve_or_abstract_geometric_primitive: Optional[Union[Polygon, LineString, Point]] = field(
        default=None,
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
