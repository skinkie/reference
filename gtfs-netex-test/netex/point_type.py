from dataclasses import dataclass, field

from .abstract_geometric_primitive_type import AbstractGeometricPrimitiveType
from .pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class PointType(AbstractGeometricPrimitiveType):
    pos: Pos = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
