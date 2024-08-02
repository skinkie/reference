from dataclasses import dataclass, field

from .day_type_enumeration import DayTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DayType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DayTypeEnumeration = field(
        default=DayTypeEnumeration.EVERY_DAY,
        metadata={
            "required": True,
        },
    )
