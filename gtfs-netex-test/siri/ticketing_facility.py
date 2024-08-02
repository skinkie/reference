from dataclasses import dataclass, field

from .ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TicketingFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
