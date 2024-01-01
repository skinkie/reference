from dataclasses import dataclass
from .point_type import PointType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Point1(PointType):
    class Meta:
        name = "Point"
        namespace = "http://www.opengis.net/gml/3.2"
