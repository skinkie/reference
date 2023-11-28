from dataclasses import dataclass
from netex.direct_position_type import DirectPositionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class VectorType(DirectPositionType):
    """
    For some applications the components of the position may be adjusted to yield a
    unit vector.
    """
