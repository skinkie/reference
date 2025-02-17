from dataclasses import dataclass

from .site_path_link_ref_structure import SitePathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SitePathLinkRef(SitePathLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
