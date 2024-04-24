from dataclasses import dataclass

from .site_path_link_ref_structure import SitePathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkRef(SitePathLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
