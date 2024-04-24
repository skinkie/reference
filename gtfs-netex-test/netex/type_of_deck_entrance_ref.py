from dataclasses import dataclass

from .type_of_deck_entrance_ref_structure import TypeOfDeckEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeckEntranceRef(TypeOfDeckEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
