from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccommodationAccessEnumeration(Enum):
    OTHER = "other"
    FREE_SEATING = "freeSeating"
    RESERVATION = "reservation"
    STANDING = "standing"
