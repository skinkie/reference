from dataclasses import dataclass
from netex.service_frame_ref_structure import ServiceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFrameRef(ServiceFrameRefStructure):
    """
    Reference to a SERVICE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
