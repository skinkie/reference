from dataclasses import dataclass, field
from netex.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingServiceFacility:
    """Classification of TICKETING FACILITY type - TPEG pti23."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
