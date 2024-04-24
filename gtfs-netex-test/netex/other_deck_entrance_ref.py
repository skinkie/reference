from dataclasses import dataclass

from .other_deck_entrance_ref_structure import OtherDeckEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckEntranceRef(OtherDeckEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
