from dataclasses import dataclass

from .deck_navigation_path_ref_structure import DeckNavigationPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckNavigationPathRef(DeckNavigationPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
