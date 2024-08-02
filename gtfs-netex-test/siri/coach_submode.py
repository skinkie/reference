from dataclasses import dataclass, field

from .coach_submodes_of_transport_enumeration import CoachSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CoachSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: CoachSubmodesOfTransportEnumeration = field(
        default=CoachSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
