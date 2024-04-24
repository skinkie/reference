from dataclasses import dataclass

from .deck_navigation_path_version_structure import DeckNavigationPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckNavigationPath(DeckNavigationPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
