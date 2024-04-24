from dataclasses import dataclass

from .site_path_link_version_structure import SitePathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLink(SitePathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
