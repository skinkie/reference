from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class KeyValueStructure:
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    type_of_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfKey",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
