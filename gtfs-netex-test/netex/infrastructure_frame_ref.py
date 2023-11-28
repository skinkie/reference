from dataclasses import dataclass
from netex.infrastructure_frame_ref_structure import InfrastructureFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureFrameRef(InfrastructureFrameRefStructure):
    """
    Reference to an INFRASTRUCTURE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
