from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupTicketingEnumeration(Enum):
    """
    Allowed values for GROUP TICKETING.
    """
    ALL_ON_ONE_TICKET = "allOnOneTicket"
    SEPARATE_TICKETS = "separateTickets"
    TICKET_WITH_COUPONS = "ticketWithCoupons"
    OTHER = "other"
