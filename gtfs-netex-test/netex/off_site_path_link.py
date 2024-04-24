from dataclasses import dataclass

from .off_site_path_link_version_structure import OffSitePathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OffSitePathLink(OffSitePathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
