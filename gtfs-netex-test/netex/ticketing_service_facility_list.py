from dataclasses import dataclass, field
from typing import List
from netex.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingServiceFacilityList:
    """List of TICKETING SERVICE FACILITies, e.g. purchase, collection.

    top up.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
