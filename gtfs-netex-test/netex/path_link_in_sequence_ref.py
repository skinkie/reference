from dataclasses import dataclass

from .path_link_in_sequence_ref_structure import PathLinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PathLinkInSequenceRef(PathLinkInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
