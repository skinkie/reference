from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScopeOfTicketEnumeration(Enum):
    UNKNOWN = "unknown"
    LOCAL_TICKET = "localTicket"
    NATIONAL_TICKET = "nationalTicket"
    INTERNATIONAL_TICKET = "internationalTicket"
