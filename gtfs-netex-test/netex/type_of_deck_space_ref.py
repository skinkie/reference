from dataclasses import dataclass

from .type_of_deck_space_profile_ref_structure import TypeOfDeckSpaceProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeckSpaceRef(TypeOfDeckSpaceProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
