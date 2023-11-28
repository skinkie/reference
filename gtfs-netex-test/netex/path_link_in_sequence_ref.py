from dataclasses import dataclass
from netex.path_link_in_sequence_ref_structure import PathLinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkInSequenceRef(PathLinkInSequenceRefStructure):
    """Reference to a PATH LINK IN SEQUENCE.

    If given by context does not need to be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
