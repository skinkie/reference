from dataclasses import dataclass
from .abstract_geometric_primitive_type import AbstractGeometricPrimitiveType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractCurveType(AbstractGeometricPrimitiveType):
    pass
