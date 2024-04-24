from dataclasses import dataclass

from .type_of_deck_space_value_structure import TypeOfDeckSpaceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeckSpace(TypeOfDeckSpaceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
