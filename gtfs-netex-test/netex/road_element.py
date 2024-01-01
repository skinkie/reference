from dataclasses import dataclass
from .road_element_version_structure import RoadElementVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadElement(RoadElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
