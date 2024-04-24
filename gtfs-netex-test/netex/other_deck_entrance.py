from dataclasses import dataclass

from .other_deck_entrance_version_structure import OtherDeckEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckEntrance(OtherDeckEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
