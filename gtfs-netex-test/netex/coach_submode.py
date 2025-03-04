from dataclasses import dataclass, field

from .coach_submode_enumeration import CoachSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CoachSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CoachSubmodeEnumeration = field(
        default=CoachSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
