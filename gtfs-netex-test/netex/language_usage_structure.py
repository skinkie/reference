from dataclasses import dataclass, field

from .language_use_enumeration import LanguageUseEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LanguageUsageStructure:
    language: str = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    language_use: list[LanguageUseEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LanguageUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
