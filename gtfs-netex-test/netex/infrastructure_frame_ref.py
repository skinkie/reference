from dataclasses import dataclass

from .infrastructure_frame_ref_structure import InfrastructureFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfrastructureFrameRef(InfrastructureFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
