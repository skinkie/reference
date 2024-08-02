from dataclasses import dataclass, field

from .rail_submodes_of_transport_enumeration import RailSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RailSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RailSubmodesOfTransportEnumeration = field(
        default=RailSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
