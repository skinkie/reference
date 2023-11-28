from dataclasses import dataclass
from netex.direct_position_list_type import DirectPositionListType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"
