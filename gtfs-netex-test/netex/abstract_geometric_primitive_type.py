from dataclasses import dataclass
from netex.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractGeometricPrimitiveType(AbstractGeometryType):
    """Gml:AbstractGeometricPrimitiveType is the abstract root type of the
    geometric primitives.

    A geometric primitive is a geometric object that is not decomposed
    further into other primitives in the system. All primitives are
    oriented in the direction implied by the sequence of their
    coordinate tuples.
    """
