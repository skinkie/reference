from dataclasses import dataclass

from .navigation_path_version_structure import NavigationPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPath(NavigationPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
