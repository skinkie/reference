from dataclasses import dataclass
from netex.polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class Polygon(PolygonType):
    """A Polygon is a special surface that is defined by a single surface patch
    (see D.3.6).

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. The elements exterior and interior
    describe the surface boundary of the polygon.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
