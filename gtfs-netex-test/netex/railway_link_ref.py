from dataclasses import dataclass
from .railway_link_ref_structure import RailwayLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRef(RailwayLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
