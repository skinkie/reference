from dataclasses import dataclass, field
from netex.ticketing_service_version_structure import TicketingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingService(TicketingServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE for ticketing, providing ticket counter and
    online purchase information, also associated with payment method and TYPE OF
    TICKET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
