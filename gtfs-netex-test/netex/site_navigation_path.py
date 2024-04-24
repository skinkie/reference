from dataclasses import dataclass

from .site_navigation_path_version_structure import SiteNavigationPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteNavigationPath(SiteNavigationPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
