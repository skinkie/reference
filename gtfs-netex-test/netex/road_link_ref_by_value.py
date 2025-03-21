from dataclasses import dataclass

from .road_link_ref_by_value_structure import RoadLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoadLinkRefByValue(RoadLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
