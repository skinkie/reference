from dataclasses import dataclass
from netex.point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class Point1(PointType):
    """A Point is defined by a single coordinate tuple.

    The direct position of a point is specified by the pos element which
    is of type DirectPositionType.
    """
    class Meta:
        name = "Point"
        namespace = "http://www.opengis.net/gml/3.2"
