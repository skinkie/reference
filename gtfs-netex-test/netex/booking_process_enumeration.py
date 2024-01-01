from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingProcessEnumeration(Enum):
    PRODUCT_NOT_AVAILABLE = "productNotAvailable"
    PRODUCT_NOT_BOOKABLE = "productNotBookable"
    BOOKABLE_THROUGH_INTERNATIONAL_SYSTEM = (
        "bookableThroughInternationalSystem"
    )
    BOOKABLE_THROUGH_NATIONAL_SYSTEM = "bookableThroughNationalSystem"
    BOOKABLE_MANUALLLY = "bookableManuallly"
    OTHER = "other"
