from dataclasses import dataclass
from netex.path_link_ref_structure import PathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SitePathLinkRefStructure(PathLinkRefStructure):
    """
    Type for Unique Reference to SITE PATH LINK.
    """
