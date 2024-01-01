from dataclasses import dataclass
from .site_version_frame_structure import SiteVersionFrameStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFrame(SiteVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
