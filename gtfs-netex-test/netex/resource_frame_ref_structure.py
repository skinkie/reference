from dataclasses import dataclass
from netex.version_frame_ref_structure import VersionFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResourceFrameRefStructure(VersionFrameRefStructure):
    """
    Type for a reference to a RESOURCE FRAME.
    """
