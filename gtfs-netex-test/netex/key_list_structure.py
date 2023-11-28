from dataclasses import dataclass, field
from typing import List
from netex.key_value_structure import KeyValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class KeyListStructure:
    """
    Type for a Key List.

    :ivar key_value: Key value pair for Entity.
    """
    key_value: List[KeyValueStructure] = field(
        default_factory=list,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
