from dataclasses import dataclass
from netex.navigation_path_ref_structure import NavigationPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathRef(NavigationPathRefStructure):
    """
    Reference to a NAVIGATION PATH.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
