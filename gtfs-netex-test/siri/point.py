from dataclasses import dataclass

from .point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Point(PointType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
