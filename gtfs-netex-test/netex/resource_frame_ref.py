from dataclasses import dataclass

from .resource_frame_ref_structure import ResourceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ResourceFrameRef(ResourceFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
