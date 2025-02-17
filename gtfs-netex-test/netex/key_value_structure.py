from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class KeyValueStructure:
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
        },
    )
