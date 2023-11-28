from dataclasses import dataclass
from netex.path_link_derived_view_structure import PathLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkView(PathLinkDerivedViewStructure):
    """
    A VIEW of a PATH LINK used to select items for presentation.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
