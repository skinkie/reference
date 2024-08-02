from dataclasses import dataclass, field

from .funicular_submodes_of_transport_enumeration import FunicularSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FunicularSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FunicularSubmodesOfTransportEnumeration = field(
        default=FunicularSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
