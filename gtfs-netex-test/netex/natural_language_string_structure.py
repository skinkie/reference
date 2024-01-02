from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NaturalLanguageStringStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
