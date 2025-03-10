from dataclasses import dataclass

from .line_string_type import LineStringType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class LineString(LineStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
