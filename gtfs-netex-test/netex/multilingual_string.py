from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MultilingualString:
    """
    Type for a string in a specified language.

    :ivar value:
    :ivar lang: Language of string contents.
    :ivar text_id_type: Resource id of string.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    text_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "textIdType",
            "type": "Attribute",
        }
    )
