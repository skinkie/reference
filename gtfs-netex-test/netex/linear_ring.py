from dataclasses import dataclass
from netex.linear_ring_type import LinearRingType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class LinearRing(LinearRingType):
    """A LinearRing is defined by four or more coordinate tuples, with linear
    interpolation between them; the first and last coordinates shall be coincident.

    The number of direct positions in the list shall be at least four.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
