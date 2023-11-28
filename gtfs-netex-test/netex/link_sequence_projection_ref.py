from dataclasses import dataclass
from netex.link_sequence_projection_ref_structure import LinkSequenceProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkSequenceProjectionRef(LinkSequenceProjectionRefStructure):
    """
    Reference to a LINK SEQUENCE PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
