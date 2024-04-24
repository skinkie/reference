from dataclasses import dataclass

from .site_navigation_path_ref_structure import SiteNavigationPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteNavigationPathRef(SiteNavigationPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
