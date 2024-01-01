from dataclasses import dataclass
from .site_path_link_version_structure import SitePathLinkVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathLink(SitePathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
