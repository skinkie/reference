from dataclasses import dataclass, field
from typing import Optional

from .deck_entrance_ref_structure import DeckEntranceRefStructure
from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceCoupleVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "DeckEntranceCouple_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_deck_entrance_ref: DeckEntranceRefStructure = field(
        metadata={
            "name": "FromDeckEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_deck_entrance_ref: DeckEntranceRefStructure = field(
        metadata={
            "name": "ToDeckEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
