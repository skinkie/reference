from dataclasses import dataclass, field

from .water_submodes_of_transport_enumeration import WaterSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class WaterSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: WaterSubmodesOfTransportEnumeration = field(
        default=WaterSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
