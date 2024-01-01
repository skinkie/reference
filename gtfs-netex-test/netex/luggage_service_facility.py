from dataclasses import dataclass, field
from .luggage_service_facility_enumeration import (
    LuggageServiceFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
