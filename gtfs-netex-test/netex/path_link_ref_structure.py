from dataclasses import dataclass
from netex.link_ref_structure import LinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkRefStructure(LinkRefStructure):
    """
    Type for a reference to a PATH LINK.
    """
