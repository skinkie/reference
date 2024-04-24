from dataclasses import dataclass

from .generic_navigation_path_version_structure import GenericNavigationPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericNavigation(GenericNavigationPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
