from dataclasses import dataclass

from .version_frame_ref_structure import VersionFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteFrameRefStructure(VersionFrameRefStructure):
    pass
