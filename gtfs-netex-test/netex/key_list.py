from dataclasses import dataclass

from .key_list_structure import KeyListStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class KeyList(KeyListStructure):
    class Meta:
        name = "keyList"
        namespace = "http://www.netex.org.uk/netex"
