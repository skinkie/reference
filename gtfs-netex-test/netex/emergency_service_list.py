from dataclasses import dataclass, field
from typing import List
from .emergency_service_enumeration import EmergencyServiceEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmergencyServiceList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
