from dataclasses import dataclass
from netex.site_frame_ref_structure import SiteFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteFrameRef(SiteFrameRefStructure):
    """
    Reference to a SITE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
