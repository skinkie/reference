from dataclasses import dataclass, field
from netex.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType
from netex.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class PointType(AbstractGeometricPrimitiveType):
    pos: Pos = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
