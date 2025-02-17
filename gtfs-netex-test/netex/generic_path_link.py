from dataclasses import dataclass

from .generic_path_link_version_structure import GenericPathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GenericPathLink(GenericPathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
