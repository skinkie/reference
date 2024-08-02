from dataclasses import dataclass, field

from .timetable_type_enumeration import TimetableTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetableType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TimetableTypeEnumeration = field(
        default=TimetableTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
