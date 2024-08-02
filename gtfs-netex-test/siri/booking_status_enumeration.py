from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class BookingStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    LIMITED = "limited"
    VERY_LIMITED = "veryLimited"
    FULL = "full"
    WAITING_LIST = "waitingList"
    NO_BOOKING_REQUIRED = "noBookingRequired"
    BOOKING_REQUIRED = "bookingRequired"
    BOOKING_OPTIONAL = "bookingOptional"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"
