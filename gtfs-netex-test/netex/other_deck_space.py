from dataclasses import dataclass

from .other_deck_space_version_structure import OtherDeckSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckSpace(OtherDeckSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
