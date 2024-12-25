from dataclasses import dataclass, field

from .emergency_service_enumeration import EmergencyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmergencyServiceList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
