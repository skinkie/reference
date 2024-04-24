from dataclasses import dataclass

from .deck_path_link_ref_structure import DeckPathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPathLinkRef(DeckPathLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
