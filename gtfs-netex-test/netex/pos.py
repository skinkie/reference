from dataclasses import dataclass
from netex.direct_position_type import DirectPositionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class Pos(DirectPositionType):
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml/3.2"
