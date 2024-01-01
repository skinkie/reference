from dataclasses import dataclass
from .infrastructure_frame_ref_structure import InfrastructureFrameRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureFrameRef(InfrastructureFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
