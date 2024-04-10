from dataclasses import dataclass

from .resource_frame_version_frame_structure import ResourceFrameVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResourceFrame(ResourceFrameVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
