from dataclasses import dataclass, field
from netex.mobility_service_version_frame_structure import MobilityServiceVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceFrame(MobilityServiceVersionFrameStructure):
    """A coherent set of MOBILITY SERVICE data to which the same frame VALIDITY
    CONDITIONs have been assigned.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
