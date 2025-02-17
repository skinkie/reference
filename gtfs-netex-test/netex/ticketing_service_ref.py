from dataclasses import dataclass

from .ticketing_service_ref_structure import TicketingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TicketingServiceRef(TicketingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
