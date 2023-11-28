from dataclasses import dataclass, field
from netex.site_path_link_version_structure import SitePathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SitePathLink(SitePathLinkVersionStructure):
    """
    A PATH LINK between two nodes that are SITE components, i.e. within a STOP
    PLACE or POINT OF INTEREST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
