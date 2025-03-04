from dataclasses import dataclass

from .abstract_curve_type import AbstractCurveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class AbstractCurve(AbstractCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
