from dataclasses import dataclass, field
from typing import List
from netex.line_string import LineString

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class CurveArrayPropertyType:
    """A container for an array of curves.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements via XLinks is not
    supported.
    """
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
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
