from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccommodationAccessEnumeration(Enum):
    """
    Allowed values for Accommodation Access.

    :cvar OTHER:
    :cvar FREE_SEATING:
    :cvar RESERVATION: pti23_3
    :cvar STANDING:
    """
    OTHER = "other"
    FREE_SEATING = "freeSeating"
    RESERVATION = "reservation"
    STANDING = "standing"
