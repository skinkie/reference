from dataclasses import dataclass

from .deck_path_link_version_structure import DeckPathLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPathLink(DeckPathLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
