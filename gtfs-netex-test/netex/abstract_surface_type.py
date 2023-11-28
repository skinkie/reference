from dataclasses import dataclass
from netex.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """Gml:AbstractSurfaceType is an abstraction of a surface to support the
    different levels of complexity.

    A surface is always a continuous region of a plane.
    """
