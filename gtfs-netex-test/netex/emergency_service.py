from dataclasses import dataclass, field
from .emergency_service_enumeration import EmergencyServiceEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmergencyService:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: EmergencyServiceEnumeration = field(
        metadata={
            "required": True,
        }
    )
