from dataclasses import dataclass, field
from typing import List
from netex.language_use_enumeration import LanguageUseEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LanguageUsageStructure:
    """
    Type describing language usage properties.

    :ivar language: Language whose usage is described.
    :ivar language_use: Usages of language supported. Based on UN terms.
    """
    language: str = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    language_use: List[LanguageUseEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LanguageUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "tokens": True,
        }
    )
