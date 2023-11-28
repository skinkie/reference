from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class KeyValueStructure:
    """
    Type for a Key List.

    :ivar key: Identifier of value e.g. System.
    :ivar value: Value for alternative key.
    :ivar type_of_key: Identifier of type of key.
    """
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    type_of_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeOfKey",
            "type": "Attribute",
        }
    )
