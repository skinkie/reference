from dataclasses import dataclass

from .equipable_space_ref_structure import EquipableSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckComponentRefStructure(EquipableSpaceRefStructure):
    pass
