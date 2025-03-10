from dataclasses import dataclass, field

from .ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TicketingFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
