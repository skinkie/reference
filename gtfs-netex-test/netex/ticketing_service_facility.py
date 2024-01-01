from dataclasses import dataclass, field
from .ticketing_service_facility_enumeration import (
    TicketingServiceFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
