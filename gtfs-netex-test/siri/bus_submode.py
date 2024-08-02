from dataclasses import dataclass, field

from .bus_submodes_of_transport_enumeration import BusSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class BusSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: BusSubmodesOfTransportEnumeration = field(
        default=BusSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
