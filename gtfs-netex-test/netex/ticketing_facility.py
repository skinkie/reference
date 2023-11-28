from dataclasses import dataclass, field
from netex.ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingFacility:
    """Classification of TICKETING FACILITY type - eg TicketOffice, Machine, etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
