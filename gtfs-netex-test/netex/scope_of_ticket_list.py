from dataclasses import dataclass, field

from .scope_of_ticket_enumeration import ScopeOfTicketEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ScopeOfTicketList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
