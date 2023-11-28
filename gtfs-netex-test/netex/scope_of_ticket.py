from dataclasses import dataclass, field
from netex.scope_of_ticket_enumeration import ScopeOfTicketEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScopeOfTicket:
    """
    Classification of SCOPEs of TICKET, eg national international.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ScopeOfTicketEnumeration = field(
        default=ScopeOfTicketEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
