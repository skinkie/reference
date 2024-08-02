from dataclasses import dataclass

from .navigation_path_ref_structure import NavigationPathRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class NavigationPathRef(NavigationPathRefStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
