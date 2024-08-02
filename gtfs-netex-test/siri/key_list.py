from dataclasses import dataclass

from .key_list_structure import KeyListStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class KeyList(KeyListStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
