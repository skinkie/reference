from dataclasses import dataclass

from .deck_space_version_structure import DeckSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckSpaceVersionStructure(DeckSpaceVersionStructure):
    class Meta:
        name = "OtherDeckSpace_VersionStructure"
