from dataclasses import dataclass
from .site_frame_ref_structure import SiteFrameRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFrameRef(SiteFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
