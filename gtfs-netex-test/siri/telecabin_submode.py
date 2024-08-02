from dataclasses import dataclass, field

from .telecabin_submodes_of_transport_enumeration import TelecabinSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TelecabinSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TelecabinSubmodesOfTransportEnumeration = field(
        default=TelecabinSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
