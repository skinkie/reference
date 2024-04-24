from dataclasses import dataclass

from .generic_path_link_derived_view_structure import GenericPathLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkView(GenericPathLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
