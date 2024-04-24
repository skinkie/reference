from dataclasses import dataclass

from .type_of_deck_entrance_value_structure import TypeOfDeckEntranceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeckEntrance(TypeOfDeckEntranceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
