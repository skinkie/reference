from dataclasses import dataclass

from .generic_navigation_path_ref_structure import GenericNavigationPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericNavigationPathRef(GenericNavigationPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
