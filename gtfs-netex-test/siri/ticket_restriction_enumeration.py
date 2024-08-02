from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TicketRestrictionEnumeration(Enum):
    UNKNOWN = "unknown"
    ALL_TICKET_CLASSES_VALID = "allTicketClassesValid"
    FULL_FARE_ONLY = "fullFareOnly"
    CERTAIN_TICKETS_ONLY = "certainTicketsOnly"
    TICKET_WITH_RESERVATION = "ticketWithReservation"
    SPECIAL_FARE = "specialFare"
    ONLY_TICKETS_OF_SPECIFIED_OPERATOR = "onlyTicketsOfSpecifiedOperator"
    NO_RESTRICTIONS = "noRestrictions"
    NO_OFF_PEAK_TICKETS = "noOffPeakTickets"
    NO_WEEKEND_RETURN_TICKETS = "noWeekendReturnTickets"
    NO_REDUCED_FARE_TICKETS = "noReducedFareTickets"
    UNKNOWN_TICKET_RESTRICTION = "unknownTicketRestriction"
