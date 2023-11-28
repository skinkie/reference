from dataclasses import dataclass
from netex.line_link_ref_structure import LineLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineLinkRef(LineLinkRefStructure):
    """
    Reference to a LINE LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
