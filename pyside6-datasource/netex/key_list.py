from dataclasses import dataclass
from netex.key_list_structure import KeyListStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class KeyList(KeyListStructure):
    """
    A list of alternative Key values for an element.
    """
    class Meta:
        name = "keyList"
        namespace = "http://www.netex.org.uk/netex"
