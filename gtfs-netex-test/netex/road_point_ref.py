from dataclasses import dataclass
from .road_point_ref_structure import RoadPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadPointRef(RoadPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
