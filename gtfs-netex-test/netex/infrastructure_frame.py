from dataclasses import dataclass, field
from netex.infrastructure_version_frame_structure import InfrastructureVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureFrame(InfrastructureVersionFrameStructure):
    """
    A coherent set of infrastructure network description data to which the same
    VALIDITY CONDITIONs have been assigned.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
