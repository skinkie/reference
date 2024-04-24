from dataclasses import dataclass

from .other_deck_space_ref_structure import OtherDeckSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckSpaceRef(OtherDeckSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
