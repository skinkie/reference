from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketTypeEnumeration(Enum):
    """
    Allowed value for Ticket Types.
    """
    STANDARD = "standard"
    PROMOTION = "promotion"
    CONCESSION = "concession"
    GROUP = "group"
    SEASON = "season"
    CARNET = "carnet"
    TRAVEL_CARD = "travelCard"
    OTHER = "other"
    ALL = "all"
