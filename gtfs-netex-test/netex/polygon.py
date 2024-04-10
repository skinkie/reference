from dataclasses import dataclass

from .polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Polygon(PolygonType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
