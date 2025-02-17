from dataclasses import dataclass, field

from .ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TicketingServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
