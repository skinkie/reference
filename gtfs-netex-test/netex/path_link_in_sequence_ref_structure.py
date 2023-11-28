from dataclasses import dataclass
from netex.link_in_sequence_ref_structure import LinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkInSequenceRefStructure(LinkInSequenceRefStructure):
    """
    Type for Reference to a PATH LINK IN SEQUENCE.
    """
