from dataclasses import dataclass, field

from .metro_submodes_of_transport_enumeration import MetroSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MetroSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MetroSubmodesOfTransportEnumeration = field(
        default=MetroSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
