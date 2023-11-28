from dataclasses import dataclass, field
from netex.link_sequence_projection_version_structure import LinkSequenceProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkSequenceProjection(LinkSequenceProjectionVersionStructure):
    """
    A Projection of a whole LINK SEQUENCE as an ordered series of POINTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
