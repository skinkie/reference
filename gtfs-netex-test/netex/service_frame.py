from dataclasses import dataclass, field
from netex.service_version_frame_structure import ServiceVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFrame(ServiceVersionFrameStructure):
    """
    A coherent set of Service data to which the same frame VALIDITY CONDITIONs have
    been assigned.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
