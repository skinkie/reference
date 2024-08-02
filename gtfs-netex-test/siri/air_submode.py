from dataclasses import dataclass, field

from .air_submodes_of_transport_enumeration import AirSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AirSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AirSubmodesOfTransportEnumeration = field(
        default=AirSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
