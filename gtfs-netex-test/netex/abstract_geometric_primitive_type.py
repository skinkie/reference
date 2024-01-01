from dataclasses import dataclass
from .abstract_geometry_type import AbstractGeometryType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractGeometricPrimitiveType(AbstractGeometryType):
    pass
