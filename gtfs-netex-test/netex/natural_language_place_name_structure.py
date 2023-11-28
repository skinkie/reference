from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class NaturalLanguagePlaceNameStructure:
    """@lang. ISO language code (default is 'en')
    A string containing a phrase in a natural language name that requires at least one character of text and forbids certain reserved characters."""
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[^,\[\]\{\}\?$%\^=@#;:]+",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
