from dataclasses import dataclass
from netex.road_link_ref_by_value_structure import RoadLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadLinkRefByValue(RoadLinkRefByValueStructure):
    """
    Reference to a ROAD LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
