from dataclasses import dataclass
from .railway_element_version_structure import RailwayElementVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayElement(RailwayElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
