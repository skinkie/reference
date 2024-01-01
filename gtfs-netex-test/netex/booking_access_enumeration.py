from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingAccessEnumeration(Enum):
    PUBLIC = "public"
    AUTHORISED_PUBLIC = "authorisedPublic"
    STAFF = "staff"
    OTHER = "other"
