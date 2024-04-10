from dataclasses import dataclass, field
from typing import List

from .language_use_enumeration import LanguageUseEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LanguageUsageStructure:
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
            "tokens": True,
        },
    )
