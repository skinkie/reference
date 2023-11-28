from dataclasses import dataclass
from netex.ticketing_service_ref_structure import TicketingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketingServiceRef(TicketingServiceRefStructure):
    """
    Identifier of an TICKETING SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
