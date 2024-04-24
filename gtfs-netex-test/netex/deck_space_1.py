from dataclasses import dataclass

from .deck_space_version_structure import DeckSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpace1(DeckSpaceVersionStructure):
    class Meta:
        name = "DeckSpace"
        namespace = "http://www.netex.org.uk/netex"
