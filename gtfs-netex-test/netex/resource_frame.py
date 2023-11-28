from dataclasses import dataclass, field
from netex.resource_frame_version_frame_structure import ResourceFrameVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResourceFrame(ResourceFrameVersionFrameStructure):
    """A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs,
    VEHICLE TYPEs etc that have a common validity, as specified by a set of frame
    VALIDITY CONDITIONs.

    Used to define common resources that will be referenced by other
    types of FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
