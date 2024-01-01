from dataclasses import dataclass, field
from typing import List
from .scope_of_ticket_enumeration import ScopeOfTicketEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScopeOfTicketList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
