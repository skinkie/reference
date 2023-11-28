from dataclasses import dataclass
from netex.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """Gml:AbstractCurveType is an abstraction of a curve to support the different
    levels of complexity.

    The curve may always be viewed as a geometric primitive, i.e. is
    continuous.
    """
