from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .language_usage_structure import LanguageUsageStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LocaleStructure:
    time_zone_offset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    summer_time_zone_offset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SummerTimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    summer_time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummerTimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    languages: Optional["LocaleStructure.Languages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(slots=True, kw_only=True)
    class Languages:
        language_usage: list[LanguageUsageStructure] = field(
            default_factory=list,
            metadata={
                "name": "LanguageUsage",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
