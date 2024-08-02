from dataclasses import dataclass, field

from .tram_submodes_of_transport_enumeration import TramSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TramSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TramSubmodesOfTransportEnumeration = field(
        default=TramSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
