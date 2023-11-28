from dataclasses import dataclass, field
from typing import List
from netex.scope_of_ticket_enumeration import ScopeOfTicketEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScopeOfTicketList:
    """
    List of SCOPEs of TICKET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
