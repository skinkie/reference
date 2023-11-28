from dataclasses import dataclass, field
from typing import Optional, Union
from netex.line_string import LineString
from netex.nil_reason_enumeration_value import NilReasonEnumerationValue
from netex.point_1 import Point1
from netex.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class GeometryPropertyType:
    """A geometric property may either be any geometry element encapsulated in an
    element of this type or an XLink reference to a remote geometry element (where
    remote includes geometry elements located elsewhere in the same or another
    document).

    Note that either the reference or the contained element shall be
    given, but not both or none. If a feature has a property that takes
    a geometry element as its value, this is called a geometry property.
    A generic type for such a geometry property is GeometryPropertyType.
    """
    polygon_or_line_string_or_point: Optional[object] = field(
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
                    "type": Point1,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
