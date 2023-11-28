from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.language_usage_structure import LanguageUsageStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LocaleStructure:
    """
    Type describing common locale dependent properties.

    :ivar time_zone_offset: Timezone offset from Greenwich at LOCALE.
    :ivar time_zone: Timezone name at LOCALE.
    :ivar summer_time_zone_offset: Summer timezone offset if different
        from Time zone offset.
    :ivar summer_time_zone: Summer Time zone name at LOCALE.
    :ivar default_language: Default Language for LOCALE. Assume language
        use is "normally used"
    :ivar languages: Languages supported at LOCALE.
    """
    time_zone_offset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    summer_time_zone_offset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SummerTimeZoneOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    summer_time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummerTimeZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    languages: Optional["LocaleStructure.Languages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Languages:
        """
        :ivar language_usage: Language usage.
        """
        language_usage: List[LanguageUsageStructure] = field(
            default_factory=list,
            metadata={
                "name": "LanguageUsage",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
