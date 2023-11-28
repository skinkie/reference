from dataclasses import dataclass, field
from netex.fare_frame_version_frame_structure import FareFrameVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareFrame(FareFrameVersionFrameStructure):
    """
    A coherent set of Vehicle Scheduling data to which the same VALIDITY CONDITIONs
    have been assigned.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
